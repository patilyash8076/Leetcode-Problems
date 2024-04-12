# Write your MySQL query statement below
-- SELECT x,y,z,
--     SUM(CASE WHEN x + y > z then 1
--      WHEN y + z > x then 1
--      WHEN x + z > y then 1
--     ELSE 0) END AS total_len
-- FROM triangle

SELECT *,
    CASE WHEN x+y>z and y+z>x and x+z > y then "Yes" ELSE 'No' END AS triangle
FROM triangle