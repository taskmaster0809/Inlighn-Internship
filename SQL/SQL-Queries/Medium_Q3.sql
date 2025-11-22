SELECT track_id, name, LENGTH(name) AS name_length
FROM track
WHERE LENGTH(name) > (SELECT AVG(LENGTH(name)) FROM track)
ORDER BY name_length DESC;
