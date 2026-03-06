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