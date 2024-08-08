# Write your MySQL query statement below
-- SELECT player_id, min(event_date) as first_login
-- FROM Activity
-- GROUP BY player_id

WITH temp_cte as(
SELECT player_id,
DENSE_RANK() OVER(Partition by player_id ORDER BY event_date) as rankk,
event_date
FROM Activity)

SELECT player_id, event_date as first_login
FROM temp_cte
WHERE rankk = 1