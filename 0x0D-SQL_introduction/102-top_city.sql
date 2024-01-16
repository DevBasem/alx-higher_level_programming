-- Retrieve the top 3 cities with the highest average temperatures 
-- during July and August from the 'Temperatures' table.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
