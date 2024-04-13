# Write your MySQL query statement below
SELECT project_id, round(sum(experience_years) / count(e.experience_years ),2) as average_years 
FROM Project p
JOIN Employee e on p.employee_id = e.employee_id
GROUP BY Project_id