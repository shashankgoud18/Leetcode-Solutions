# Write your MySQL query statement below
(
select 
    u.name as 'results'
from users as u
join movieRating as mr
on u.user_id = mr.user_id
group by u.name
order by count(mr.movie_id) desc, u.name asc
limit 1
)
UNION ALL
(
select
    m.title as 'results'
from MovieRating as mr
join movies as m 
on m.movie_id =  mr.movie_id
where created_at >= '2020-02-01' and 
      created_at < '2020-03-01'
group by m.title
order by avg(mr.rating) desc, m.title asc
limit 1
)
