# Write your MySQL query statement below
select 
visited_on,(
    select
    sum(amount)
    from customer
    where visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
) as amount,
(
    select
    ROUND(sum(amount)/7,2)
    from customer
    where visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
) as average_amount
from customer c
where visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    from customer
)
group by visited_on
order by visited_on