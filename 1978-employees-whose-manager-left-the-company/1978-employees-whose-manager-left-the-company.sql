# Write your MySQL query statement below
select employee_id
from employees
where salary < 30000 and
manager_id NOT IN (
    select employee_id
    from employees
)
ORDER BY employee_id