select e.name as Employee from Employee as e, Employee as e2 where e.managerid = e2.id and e.salary > e2.salary