-- # Write your MySQL query statement below
select customer_id, count(customer_id) AS count_no_trans from visits left join transactions 
on visits.visit_id = transactions.visit_id where transaction_id is null
Group by customer_id

-- select *-- customer_id, count(v.visit_id) as count_no_trans 
-- from Visits v
-- left join Transactions t on v.visit_id = t.visit_id
-- where  transaction_id IS NULL
-- GROUP BY customer_id