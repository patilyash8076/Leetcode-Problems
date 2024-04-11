# Write your MySQL query statement below
-- SELECT employee_id, department_id 
-- FROM Employee
-- Where primary_flag = 'Y' and employee_id IN 
--     (SELECT employee_id from Employee GROUP BY Employee_id having count(employee_id) = 1)
-- SELECT employee_id from Employee GROUP BY Employee_id having count(employee_id) = 1
SELECT employee_id, department_id 
FROM Employee
Where primary_flag = 'Y'
UNION 
SELECT employee_id, department_id from Employee GROUP BY Employee_id having count(employee_id) = 1