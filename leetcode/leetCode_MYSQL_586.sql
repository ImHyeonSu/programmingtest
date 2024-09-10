# Write your MySQL query statement below
SELECT order.customer_number from order WHERE order.order_number = (SELECT MAX(order.order_number) FROM order);  

SELECT
customer_number
FROM
(SELECT SUM(order_number)), customer_number
FROM Orders
GROUP BY customer_number) ORDER BY order_number DESC
LIMIT 1;

-> 最新版
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY SUM(order_number) DESC
LIMIT 1;

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;