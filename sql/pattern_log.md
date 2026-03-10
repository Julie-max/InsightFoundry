# SQL Pattern Log

This file stores SQL query patterns learned during practice.

---

## Pattern 1 — SELECT + WHERE

Used to filter rows based on a condition.

Example query:

SELECT name, salary
FROM employees
WHERE salary > 50000;

---

## Pattern 2 — GROUP BY + SUM

Used to aggregate numeric values per category.

Example query:

SELECT category, SUM(sales)
FROM orders
GROUP BY category;

---

## Pattern 3 — GROUP BY + COUNT

Used to count rows per group.

Example query:

SELECT customer_id, COUNT(*)
FROM orders
GROUP BY customer_id;

---

## Pattern 4 — INNER JOIN
Used to combine rows from two tables when matching values exist in both.

Example query:

SELECT e.name, b.bonus
FROM Employee e
JOIN Bonus b
ON e.empId = b.empId;

---

## Pattern 5 — LEFT JOIN + NULL filtering
Used to find rows that exist in one table but not in another.

Example query:

SELECT c.customer_id
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;

---

## Pattern 6 — SELF JOIN
Used when a table needs to be joined with itself to compare rows.

Example query:

SELECT today.id
FROM Weather today
JOIN Weather yesterday
ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
AND today.temperature > yesterday.temperature;

---

## Pattern 7 — CROSS JOIN
Used to generate all combinations of rows from two tables.

Example query:

SELECT s.student_id, sub.subject_name
FROM Students s
CROSS JOIN Subjects sub;

---

## Pattern 8 — GROUP BY + HAVING
Used to filter aggregated groups after applying aggregate functions.

Example query:

SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5;

---

## Pattern 9 — Conditional COUNT using CASE
Used to count rows that satisfy a specific condition.

Example query:

SELECT user_id,
COUNT(CASE WHEN action = 'confirmed' THEN 1 END)
FROM Confirmations
GROUP BY user_id;

---

## Pattern 10 — Handling NULL results with IFNULL
Used to replace NULL values with a default value.

Example query:

SELECT IFNULL(value, 0);

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

SELECT 
    product_id,
    SUM(price * units) / SUM(units) AS weighted_average
FROM sales
GROUP BY product_id;