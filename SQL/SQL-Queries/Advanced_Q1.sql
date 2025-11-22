WITH artist_revenue AS (
    SELECT 
        il.invoice_id,
        al.artist_id,
        SUM(il.unit_price * il.quantity) AS artist_earnings
    FROM invoice_line il
    JOIN track t ON il.track_id = t.track_id
    JOIN album al ON t.album_id = al.album_id
    GROUP BY il.invoice_id, al.artist_id
)
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    art.name AS artist_name,
    ROUND(SUM(arv.artist_earnings), 2) AS amount_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
JOIN artist_revenue arv ON i.invoice_id = arv.invoice_id
JOIN artist art ON arv.artist_id = art.artist_id
GROUP BY c.customer_id, c.first_name, c.last_name, art.name
ORDER BY c.customer_id, amount_spent DESC;
