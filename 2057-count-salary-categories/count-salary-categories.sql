# Write your MySQL query statement below
with sal_categories as (
    SELECT "Low Salary" as category
    UNION ALL
    SELECT "Average Salary" as category
    UNION ALL
    SELECT "High Salary" as category
),

temp as (
SELECT *,
    CASE
        WHEN income < 20000 then "Low Salary"
        WHEN income >= 20000 and income <= 50000 then "Average Salary"
        WHEN income > 50000 then "High Salary"
        END as category
FROM Accounts )

SELECT sc.category, count(account_id) as accounts_count
FROM TEMP te
RIGHT JOIN sal_categories sc ON te.category = sc.category
GROUP BY sc.category
