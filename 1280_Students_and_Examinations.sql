# Write your MySQL query statement below
select st.student_id, st.student_name, su.subject_name, count(ex.subject_name) as attended_exams
from Students st
inner join Subjects su
left join Examinations ex
on ex.student_id = st.student_id and ex.subject_name = su.subject_name
group by st.student_id, su.subject_name
order by st.student_id;