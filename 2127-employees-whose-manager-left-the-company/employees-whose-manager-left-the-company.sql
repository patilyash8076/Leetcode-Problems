# Write your MySQL query statement below
SELECT employee_id
FROM Employees 
where manager_id not in (select employee_id from employees) and salary < 30000
ORDER BY employee_id