# Write your MySQL query statement below
with sales_cte as(
Select sales_id from Orders where com_id = (select com_id from company where name = 'RED'))

select name from SalesPerson where sales_id not in (select sales_id from sales_cte)
-- select * from sales_cte