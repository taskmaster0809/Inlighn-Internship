SELECT billing_city, ROUND(CAST(SUM(total) AS numeric), 2) AS total_invoice_amount
FROM invoice
GROUP BY billing_city
ORDER BY total_invoice_amount DESC
FETCH FIRST 1 ROWS WITH TIES;

