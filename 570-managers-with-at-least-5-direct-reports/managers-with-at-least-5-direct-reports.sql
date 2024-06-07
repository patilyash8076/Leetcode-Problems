# Write your MySQL query statement below
-- select name from employee where ID  IN (select managerID from EMPLOYEE  GROUP BY managerID having count(managerId) > 4) 
SELECT e1.name FROM EMPLOYEE e1
JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.ID
having count(e2.managerId) >= 5