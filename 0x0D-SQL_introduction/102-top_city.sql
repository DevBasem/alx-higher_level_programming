-- Display top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM your_table_name
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
