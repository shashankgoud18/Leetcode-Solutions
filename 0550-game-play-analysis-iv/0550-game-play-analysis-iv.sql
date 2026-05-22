# Write your MySQL query statement below
select ROUND(COUNT(player_id)/(select count(distinct player_id) from activity),2) as fraction
from activity
where (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))IN(
    select player_id, min(event_date) as first_date
    from activity
    group by player_id
)
