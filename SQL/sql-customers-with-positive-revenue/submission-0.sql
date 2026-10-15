-- Write your query below
select customer_id from (
select customer_id, year, sum(revenue) from customers group by customer_id,year having sum(revenue) > 0 and year = 2020
) c