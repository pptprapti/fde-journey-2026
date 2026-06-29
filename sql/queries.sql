-- ============================================
-- DAY 27: GROUP BY, Aggregate Functions, HAVING, NULL handling
-- ============================================

-- 1. Count how many employees exist per department
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- 2. Find employees with no department assigned (NULL handling)
-- Note: NULL must be checked with IS NULL, not = NULL,
-- since NULL never equals anything, including another NULL
SELECT *
FROM employees
WHERE department IS NULL;

-- 3. Total combined salary per department
SELECT department, SUM(salary)
FROM employees
GROUP BY department;

-- 4. Average salary per department
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- 5. Only show departments where total salary exceeds 70000
-- HAVING filters groups AFTER aggregation; WHERE cannot be used here
-- because SUM(salary) doesn't exist until grouping happens
SELECT department, SUM(salary)
FROM employees
GROUP BY department
HAVING SUM(salary) > 70000;

-- 6. Combined example: filter individual rows first (WHERE),
-- then group and filter the resulting groups (HAVING)
-- Execution order: WHERE runs before GROUP BY, HAVING runs after
SELECT department, SUM(salary)
FROM employees
WHERE salary > 50000
GROUP BY department
HAVING SUM(salary) > 70000;