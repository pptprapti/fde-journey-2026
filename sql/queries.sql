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

-- ============================================
-- DAY 28: JOINs - INNER JOIN and LEFT JOIN
-- ============================================

-- Setup: Create departments table
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT
);

INSERT INTO departments (id, name, location) VALUES
(1, 'IT', 'Bangalore'),
(2, 'HR', 'Mumbai'),
(3, 'Finance', 'Delhi');

-- INNER JOIN: only employees with matching department
-- Excludes Anita and Riya (NULL department)
SELECT employees.name, employees.salary, departments.location
FROM employees
INNER JOIN departments ON employees.department = departments.name;

-- LEFT JOIN: all employees, NULL location for unmatched
-- Shows Anita and Riya with NULL location
SELECT employees.name, employees.salary, departments.location
FROM employees
LEFT JOIN departments ON employees.department = departments.name;

-- Practical use: find employees with no valid department (orphaned records)
-- Real-world: data quality check in migration work
SELECT employees.name, employees.department
FROM employees
LEFT JOIN departments ON employees.department = departments.name
WHERE departments.name IS NULL;

-- ============================================
-- DAY 29: RIGHT JOIN
-- ============================================

-- RIGHT JOIN: all rows from right table (departments)
-- employees without a matching department are excluded
-- departments without matching employees would show NULL on left columns
SELECT employees.name, employees.salary,
       departments.name as dept_name, departments.location
FROM employees
RIGHT JOIN departments ON employees.department = departments.name;

-- Note: RIGHT JOIN is equivalent to swapping tables and using LEFT JOIN
-- Most developers prefer LEFT JOIN for readability
-- A RIGHT JOIN B = B LEFT JOIN A