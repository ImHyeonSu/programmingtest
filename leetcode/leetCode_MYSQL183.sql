# Write your MySQL query statement below
SELECT name as Customers FROM Customers left join Orders on Customers.id = Orders.customerId WHERE CustomerId IS NULL