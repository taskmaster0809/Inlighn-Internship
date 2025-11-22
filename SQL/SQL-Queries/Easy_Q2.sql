SELECT billing_country, COUNT(*) AS no_of_invoices
FROM invoice
GROUP BY billing_country
ORDER BY no_of_invoices DESC;