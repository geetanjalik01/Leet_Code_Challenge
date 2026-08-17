# Write your MySQL query statement below
select u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019
from Users u
LEFT JOIN Orders o 
ON u.user_id = o.buyer_id AND YEAR(order_date) = '2019'
GROUP BY u.user_id
ORDER BY u.user_id;