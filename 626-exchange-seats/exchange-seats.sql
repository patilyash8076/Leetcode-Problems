# Write your MySQL query statement below
-- SELECT
-- Row_number() OVER() AS ID, STUDENT
-- FROM SEAT
-- ORDER BY if(mod(id,2) = 0, id-1, id+1)

SELECT 
CASE WHEN ID = (SELECT MAX(ID) FROM SEAT) and ID % 2 = 1 THEN ID
     WHEN ID % 2 = 0 THEN ID-1
     WHEN ID % 2 = 1 THEN  ID+1
     END AS ID,
     STUDENT
FROM SEAT
ORDER BY ID