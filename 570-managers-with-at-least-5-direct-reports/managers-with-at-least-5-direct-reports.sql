# Write your MySQL query statement below
-- SELECT name 
-- FROM employee 
-- WHERE ID IN (
--     SELECT managerID 
--     FROM employee 
--     GROUP BY managerID 
--     HAVING COUNT(managerID) > 4
-- );
-- 2nd approach
SELECT e1.name FROM EMPLOYEE e1
JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.ID
having count(e2.managerId) >= 5