# Write your MySQL query statement below
SELECT MAX(SALARY) as SecondHighestSalary FROM EMPLOYEE 
WHERE salary not in    
    (SELECT max(salary) from Employee)
