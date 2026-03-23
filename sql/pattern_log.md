# SQL Pattern Log

This file stores SQL query patterns learned during practice.

---

## Pattern 1 — SELECT + WHERE

Used to filter rows based on a condition.

Example query:

```sql
SELECT name, salary
FROM employees
WHERE salary > 50000;
```

---

## Pattern 2 — GROUP BY + SUM

Used to aggregate numeric values per category.

Example query:

```sql
SELECT category, SUM(sales)
FROM orders
GROUP BY category;
```

---

## Pattern 3 — GROUP BY + COUNT

Used to count rows per group.

Example query:

```sql
SELECT customer_id, COUNT(*)
FROM orders
GROUP BY customer_id;
```

---

## Pattern 4 — INNER JOIN

Used to combine rows from two tables when matching values exist in both.

Example query:

```sql
SELECT e.name, b.bonus
FROM Employee e
JOIN Bonus b
ON e.empId = b.empId;
```

---

## Pattern 5 — LEFT JOIN + NULL filtering

Used to find rows that exist in one table but not in another.

Example query:

```sql
SELECT c.customer_id
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;
```

---

## Pattern 6 — SELF JOIN

Used when a table needs to be joined with itself to compare rows.

Example query:

```sql
SELECT today.id
FROM Weather today
JOIN Weather yesterday
ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
AND today.temperature > yesterday.temperature;
```

---

## Pattern 7 — CROSS JOIN

Used to generate all combinations of rows from two tables.

Example query:

```sql
SELECT s.student_id, sub.subject_name
FROM Students s
CROSS JOIN Subjects sub;
```

---

## Pattern 8 — GROUP BY + HAVING

Used to filter aggregated groups after applying aggregate functions.

Example query:

```sql
SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5;
```

---

## Pattern 9 — Conditional COUNT using CASE

Used to count rows that satisfy a specific condition.

Example query:

```sql
SELECT user_id,
       COUNT(CASE WHEN action = 'confirmed' THEN 1 END)
FROM Confirmations
GROUP BY user_id;
```

---

## Pattern 10 — Handling NULL results with IFNULL

Used to replace NULL values with a default value.

Example query:

```sql
SELECT IFNULL(value, 0);
```

---

## Pattern 11 — Weighted Average

Used when calculating an average where each value has a weight.

Formula:

SUM(value * weight) / SUM(weight)

Example use cases:

- Average selling price
- Revenue per unit
- Weighted ratings

Example query:

```sql
SELECT product_id,
       SUM(price * units) / SUM(units) AS weighted_average
FROM sales
GROUP BY product_id;
```

---

## Pattern 12 — Scalar Subquery for Global Total

Used when we need to divide a grouped metric by a global count.

Example:

```sql
SELECT contest_id,
       COUNT(*) / (SELECT COUNT(*) FROM Users)
FROM Register
GROUP BY contest_id;
```

---

## Pattern 13 — Conditional Aggregation

Used to compute counts or percentages based on a condition inside grouped data.

Idea:
Convert a boolean condition into numeric values (1 or 0) and aggregate.

Common formulas:

SUM(condition)

or

SUM(CASE WHEN condition THEN 1 ELSE 0 END)

Example use cases:
- Percentage of failed queries
- Conversion rates
- Error rates
- Success ratios

Example query:

```sql
SELECT query_name,
       ROUND((SUM(rating < 3) / COUNT(*)) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```

---

## Pattern 14 — Selecting First Row per Group

Used when we need to select the earliest (or latest) record for each entity.

Common analytics examples:
- first purchase per customer
- first login per user
- earliest transaction
- latest event

This pattern appeared in the **Immediate Food Delivery II** problem.


### Approach 1 — Correlated Subquery

Filters rows by comparing them with an aggregate value computed for the same group.

Example query:

```sql
SELECT *
FROM Delivery d
WHERE d.order_date = (
    SELECT MIN(order_date)
    FROM Delivery
    WHERE customer_id = d.customer_id
);
```

Concept:

For each row, check if the order date equals the earliest order date for that customer.

Pros:
- Easy to understand.

Cons:
- Subquery may run once per row.
- Can be slower on large datasets.


### Approach 2 — Tuple Comparison with IN

Compute the grouped result first and filter rows using tuple matching.

Example query:

```sql
SELECT *
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);
```

Concept:

Create a set of `(customer_id, first_order_date)` pairs and keep rows that match.

Pros:
- Subquery runs once.
- More efficient than correlated subqueries.

Cons:
- Slightly less explicit logic.


### Approach 3 — JOIN with Aggregated Result (Preferred)

Create a derived table containing the first record per group and join it back to the original table.

Example query:

```sql
SELECT *
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
) f
ON d.customer_id = f.customer_id
AND d.order_date = f.first_order;
```

Concept:

1. Compute earliest order per customer.
2. Join it with the main table to retrieve the correct rows.

Pros:
- Clear logic.
- Efficient execution.
- Easy to extend with additional columns.

This is the **preferred approach in most production SQL queries**.


### Key Insight

Many SQL problems reduce to:

```
Find earliest or latest row per group
```

Understanding these three approaches allows solving many analytics queries efficiently.

---

## Pattern 15 — First Event + Next Event Check

Used to identify entities where an initial event is followed by another event with a specific time condition (e.g., next day login).

Idea:
First compute the initial event per entity, then check if a related event exists by comparing rows within the same table.

Common steps:

1. Get first event per entity using aggregation
2. Compare with other rows using a join (same table)
3. Filter based on time condition (e.g., +1 day)
4. Count distinct entities if needed

Example use cases:
- Users who return the next day
- Repeat purchases within 24 hours
- Consecutive activity tracking
- Retention analysis

Example query:

```sql
SELECT ROUND(COUNT(DISTINCT a2.player_id) * 1.0 / COUNT(DISTINCT a1.player_id), 2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) a1
LEFT JOIN Activity a2
ON a1.player_id = a2.player_id
AND a2.event_date = DATE_ADD(a1.first_login, INTERVAL 1 DAY);
```

---

## Pattern 16 — First/Minimum per Group (Join Back)

Used when you need to retrieve the full row corresponding to a minimum (or maximum) value within each group.

Idea:
First compute the minimum (or maximum) value per group using GROUP BY, then join this result back to the original table to retrieve the full row.

Why this pattern is needed:
GROUP BY collapses rows and only returns aggregated values, so we lose access to other columns. To retrieve full row details (like quantity, price), we must join back with the original table.

Common use cases:
- First sale per product
- Earliest login per user
- Cheapest product per category
- Latest transaction per account

Example query:

```sql
SELECT t1.*
FROM table t1
JOIN (
    SELECT group_col, MIN(value_col) AS min_val
    FROM table
    GROUP BY group_col
) t2
ON t1.group_col = t2.group_col 
AND t1.value_col = t2.min_val;
```

---

## Pattern 17 — Aggregation + Outer Query (2-Step Pattern)

Used when a problem requires:
- filtering based on aggregated values
- AND then applying further operations (like MAX, sorting, or selection)

Idea:
Break the problem into two steps:
1. Inner query → compute grouped/filtered results
2. Outer query → apply final operation on the result set

Why this pattern is needed:
Complex queries often cannot be solved in a single step, especially when aggregation results need further processing. Separating logic improves clarity and correctness.

Common use cases:
- Find max/min among filtered groups
- Rank or sort aggregated results
- Apply additional filtering after aggregation

Example:

```sql
SELECT MAX(num)
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;
```

---

# 📘 Pattern 18 — Safe Aggregation for Empty Results

```markdown
## Pattern 18 — Safe Aggregation for Empty Results (MAX/MIN Wrapper)

Used when a query may return no rows, but the problem requires a single value (e.g., NULL instead of empty result).

Idea:
Wrap the result in an aggregate function like MAX() or MIN() so that:
- If rows exist → returns correct value
- If no rows exist → returns NULL automatically

Why this pattern is needed:
Some queries return empty result sets, but problems may expect a scalar output. Aggregate functions ensure safe output handling.

Common use cases:
- Largest/smallest value queries
- Conditional queries with possible no results
- Avoiding empty result outputs

Example:

```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;
```

---