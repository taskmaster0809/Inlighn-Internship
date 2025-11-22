WITH amount_per_customer_per_country AS (
	SELECT i.billing_country, i.customer_id, c.first_name, c.last_name, 
	       ROUND(CAST(SUM(i.total) AS NUMERIC), 2) AS total_amount_spent
	FROM customer c JOIN invoice i
	USING(customer_id)
	GROUP BY i.billing_country, i.customer_id, c.first_name, c.last_name
)

SELECT billing_country AS country, customer_id AS top_spending_customer_id, first_name, last_name, total_amount_spent FROM (
	SELECT *, 
	       RANK() OVER(PARTITION BY billing_country ORDER BY total_amount_spent DESC) AS rn
	FROM amount_per_customer_per_country
) AS ranked
WHERE rn = 1;
