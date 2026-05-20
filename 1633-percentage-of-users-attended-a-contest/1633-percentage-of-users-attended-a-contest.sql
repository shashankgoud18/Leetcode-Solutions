# Write your MySQL query statement below
SELECT r.contest_id, ROUND((count(contest_id)/(SELECT COUNT(*) FROM Users))*100,2) as percentage
FROM Users as u
INNER JOIN Register as r
ON u.user_id = r.user_id
group by r.contest_id
order by percentage desc,r.contest_id asc