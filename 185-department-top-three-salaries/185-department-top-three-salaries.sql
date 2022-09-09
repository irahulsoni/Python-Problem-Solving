# Write your MySQL query statement below
# select d.name, e.name, e.salary,
# dense_rank() over(partition by e.salary order by e.salary DESC)
# from Employee as e join Department as d on e.departmentId = d.id
#  order by e.salary desc

SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary 
FROM Employee E, Department D
WHERE (SELECT COUNT(DISTINCT(Salary)) FROM Employee 
       WHERE DepartmentId = E.DepartmentId AND Salary > E.Salary) < 3
AND E.DepartmentId = D.Id 
ORDER by E.DepartmentId, E.Salary DESC;