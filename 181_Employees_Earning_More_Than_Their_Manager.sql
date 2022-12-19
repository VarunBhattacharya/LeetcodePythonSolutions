# Write your MySQL query statement below
select e.name as Employee
from
Employee as e
join
Employee as b
on e.managerId = b.Id
and e.salary > b.salary;