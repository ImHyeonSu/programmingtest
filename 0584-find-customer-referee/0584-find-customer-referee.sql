# Write your MySQL query statement below
SELECT Customer.name 
FROM Customer 
WHERE COALESCE(Customer.referee_id, -1) != 2;