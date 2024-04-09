# Write your MySQL query statement below
select pc.product_id,
Coalesce(round(sum(pc.price * us.units) / sum(us.units),2),0) as average_price 
from prices pc
left join Unitssold us on pc.product_id =  us.product_id and purchase_date between start_date and end_date
Group by product_id