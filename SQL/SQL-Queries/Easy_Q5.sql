SELECT c.customer_id, c.first_name, c.last_name, c.country,
	   ROUND(CAST(SUM(i.total) AS NUMERIC), 2) AS total_invoice
FROM customer c LEFT JOIN invoice i
USING(customer_id)
GROUP BY c.customer_id, c.first_name, c.last_name, c.country
ORDER BY total_invoice DESC
FETCH FIRST 1 ROWS WITH TIES;
