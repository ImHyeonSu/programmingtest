# Write your MySQL query statement below
SELECT Employee.name AS Employee 
FROM Employee 
INNER JOIN Employee AS e1 
ON Employee.managerId = e1.id 
WHERE Employee.salary > e1.salary