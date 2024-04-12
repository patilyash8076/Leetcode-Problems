-- # Write your MySQL query statement below


-- select * from logs order by id

SELECT DISTINCT i1.num AS ConsecutiveNums
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE
i1.id = i2.id+1 and
i2.id = i3.id+1 and
i1.num = i2.num and
i2.num = i3.num

-- WITH cte AS (
--     SELECT num,
--            LEAD(num, 1) OVER (ORDER BY id) AS num1,
--            LEAD(num, 2) OVER (ORDER BY id) AS num2
--     FROM Logs
-- )
-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM cte
-- WHERE num = num1 AND num1 = num2;

