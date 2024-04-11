-- # Write your MySQL query statement below
-- SELECT 1 FROM 
-- (SELECT num, IF (CASE count(num) >1 then NULL ELSE 1 END) from mynumbers GROUP BY num having count(num) = 1 ORDER BY num desc limit 1) as temp
-- FROM TEMP
with temp as
(SELECT num, count(num) as unique_num from mynumbers GROUP BY num having count(num) = 1 ORDER BY num DESC LIMIT 1)
select (CASE WHEN count(num) = 0 then null ELSE num END) as num from temp