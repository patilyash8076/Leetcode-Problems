# Write your MySQL query statement below
SELECT em1.employee_id, em1.name, count(em2.reports_to) as reports_count , round(avg(em2.age)) as average_age 
FROM EMPLOYEES Em1
JOIN Employees Em2 ON Em1.employee_id = Em2.reports_to
GROUP BY em1.employee_id
ORDER BY em1.employee_id