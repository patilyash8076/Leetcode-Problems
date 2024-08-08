# Write your MySQL query statement below
-- with sales_cte as(
-- Select sales_id from Orders where com_id = (select com_id from company where name = 'RED'))
-- select name from SalesPerson where sales_id not in (select sales_id from sales_cte)

WITH sales_cte as
(SELECT sales_id FROM Orders 
     WHERE com_id = (SELECT com_id FROM company WHERE name = 'RED'))

SELECT name FROM SalesPerson  
WHERE sales_id NOT IN (SELECT * FROM sales_cte)