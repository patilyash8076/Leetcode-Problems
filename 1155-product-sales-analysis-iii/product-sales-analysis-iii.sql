-- # Write your MySQL query statement below
select product_id, year as first_year, quantity, price from sales where (product_id, year) In (select product_id, min(year) from sales group by product_id)
-- select min(year), product_id from sales group by product_id