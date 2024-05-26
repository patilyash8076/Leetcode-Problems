# Write your MySQL query statement below
SELECT
Row_number() OVER() AS ID, STUDENT
FROM SEAT
ORDER BY if(mod(id,2) = 0, id-1, id+1)