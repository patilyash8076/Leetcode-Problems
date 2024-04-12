-- # Write your MySQL query statement below
-- with cte as(
    
--     SELECT num,
--     lead(num,1) OVER(ORDER by ID) as num1,
--     LEAD(num ,2) OVER(ORDER by ID) as num2
--     FROM LOGS
-- )
-- select DISTINCT num as ConsecutiveNums
-- From cte where num=num1 and num=num2

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

