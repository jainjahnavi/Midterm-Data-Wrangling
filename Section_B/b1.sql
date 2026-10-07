SELECT c.city, SUM(o.amount) AS total_amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 1000
ORDER BY total_amount DESC;
