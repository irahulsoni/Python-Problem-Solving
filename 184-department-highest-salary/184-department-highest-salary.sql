# Write your MySQL query statement below
select department.name as department ,employee.name as employee ,salary as salary 
from employee,department 
where employee.departmentid=department.id 
and 
employee.salary =(select max(salary) from employee where employee.departmentid=department.id);
