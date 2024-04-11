# Write your MySQL query statement below
SELECT Class
FROM Courses
group by class
having count(student) > 4