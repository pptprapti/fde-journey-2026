## Day 27: GROUP BY, Aggregates, HAVING

### Concepts Learned
- GROUP BY collapses multiple rows sharing a value into one summary row per group
- COUNT(*), SUM(), AVG() - aggregate functions applied within each group
- HAVING filters groups AFTER aggregation; WHERE filters individual rows BEFORE aggregation
- Execution order: FROM -> WHERE -> GROUP BY -> aggregate functions -> HAVING

### Key Gotcha: NULL and GROUP BY
- NULL never equals anything in SQL, not even another NULL (use IS NULL, not = NULL)
- GROUP BY makes a specific exception: it groups all NULLs into a single bucket
- This can hide data quality issues in real datasets if not checked

### WHERE vs HAVING
- WHERE: filters raw rows before grouping (e.g., salary > 50000)
- HAVING: filters aggregated groups after grouping (e.g., SUM(salary) > 70000)
- Cannot use WHERE with aggregate functions, since they don't exist yet at that stage

### Real Data Finding
- employees table had 2 rows with NULL department (Anita, Riya)
- Verified via SUM: NULL group total (95000) = Anita (45000) + Riya (50000)

## Day 28: JOINs

### INNER JOIN
- Returns only rows with matches in BOTH tables
- Unmatched rows are excluded entirely (silently drops them)
- Use when you want only complete, valid, matched records

### LEFT JOIN
- Returns ALL rows from the left table (FROM table)
- Fills right table columns with NULL where no match exists
- Use when you need the full picture including gaps/missing data

### Key Real-World Pattern
- LEFT JOIN + WHERE right_table.column IS NULL = find orphaned/unmatched records
- Directly useful for data migration validation (finding records with missing foreign keys)

### Why ID-based joins are better than text-based joins
- Integer comparisons faster than string comparisons at scale
- Name changes only need updating in one place (departments table)
- IDs guaranteed unique; text can have typos, case differences, trailing spaces

### INNER vs LEFT JOIN decision
- INNER JOIN: intentionally exclude incomplete records (clean reporting)
- LEFT JOIN: show everything including gaps (data quality checks, audits)