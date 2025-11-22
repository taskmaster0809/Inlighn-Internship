WITH purchase_count_by_country AS (
	SELECT i.billing_country, g.name, COUNT(*) AS purchase_count
	FROM invoice i 
	JOIN invoice_line il ON i.invoice_id = il.invoice_id
	JOIN track t ON il.track_id = t.track_id
	JOIN genre g ON t.genre_id = g.genre_id
	GROUP BY i.billing_country, g.name 
)

SELECT billing_country AS country, name AS most_popular_genre, purchase_count FROM (
	SELECT *, 
	       RANK() OVER(PARTITION BY billing_country ORDER BY purchase_count DESC) AS rn
 	FROM purchase_count_by_country
) AS ranked_counts
WHERE rn = 1;
