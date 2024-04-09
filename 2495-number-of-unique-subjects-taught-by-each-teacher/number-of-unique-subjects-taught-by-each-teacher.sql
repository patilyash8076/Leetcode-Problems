# Write your MySQL query statement below
select teacher_id, count(Distinct subject_id) as cnt
from Teacher
GROUP BY teacher_id