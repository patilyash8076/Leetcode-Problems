-- # Write your MySQL query statement below

with temp as
(SELECT num, count(num) as unique_num from mynumbers GROUP BY num having count(num) = 1 ORDER BY num DESC LIMIT 1)
select (CASE WHEN count(num) = 0 then null ELSE num END) as num from temp 