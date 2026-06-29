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