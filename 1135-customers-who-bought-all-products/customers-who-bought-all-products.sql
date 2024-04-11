-- # Write your MySQL query statement below
SELECT customer_id from customer GROUP BY customer_id having count(DISTINCT customer_id, Product_key) = (SELECT count(product_key) from product)
-- SELECT count(product_key) from product