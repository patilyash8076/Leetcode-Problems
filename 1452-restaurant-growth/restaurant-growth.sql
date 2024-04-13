# Write your MySQL query statement below

SELECT VISITED_ON, amount, ROUND(amount/7,2) AS  average_amount FROM
    (SELECT distinct visited_on,
        SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) as amount, 
        MIN(visited_on) OVER() min_date 
        FROM Customer) AS TEMP_TABLE
WHERE VISITED_ON >= min_date + 6 
    