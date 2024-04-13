-- # Write your MySQL query statement below
SELECT customer_id 
FROM customer 
GROUP BY customer_id 
HAVING count(DISTINCT Product_key) = (SELECT count(DISTINCT product_key) from product)
