# Write your MySQL query statement below

SELECT VISITED_ON, AMOUNT, ROUND(AMOUNT/7,2) AS  average_amount FROM
    (SELECT distinct visited_on,
        SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) amount, 
        MIN(visited_on) OVER() 1st_date 
        FROM Customer) AS TEMP_TABLE
WHERE VISITED_ON >= 1st_date+6 
    