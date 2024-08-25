# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login FROM activity Group by player_id
