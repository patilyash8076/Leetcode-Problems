-- # Write your MySQL query statement below
select product_id, year as first_year, quantity, price 
from sales 
where (product_id, year) In (select s.product_id, min(year) from sales s group by 1)
-- select min(year), product_id from sales group by product_id