SELECT invoice_id, ROUND(CAST(total AS numeric), 2) AS total
FROM (
    SELECT invoice_id, total,
           DENSE_RANK() OVER (ORDER BY total DESC) AS rank_total
    FROM invoice
) 
WHERE rank_total <= 3;

