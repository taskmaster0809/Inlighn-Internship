SELECT art.name, COUNT(*) AS track_count FROM artist art
JOIN album al ON art.artist_id = al.artist_id 
JOIN track t ON al.album_id = t.album_id
JOIN genre g ON t.genre_id = g.genre_id
WHERE g.name = 'Rock'
GROUP BY art.name
ORDER BY track_count DESC
FETCH FIRST 10 ROWS WITH TIES;