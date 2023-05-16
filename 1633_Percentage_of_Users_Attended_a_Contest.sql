# Write your MySQL query statement below
select r.contest_id, round((count(distinct r.user_id)/(select count(*) from Users u))*100,2) as percentage
from Users u
left join Register r
on u.user_id = r.user_id
where r.user_id is not Null
group by r.contest_id
order by percentage desc, r.contest_id asc;