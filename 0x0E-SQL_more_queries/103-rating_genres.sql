-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum.
-- Results must be sorted in descending order by their rating.
-- You can use only one SELECT statement.
-- The database name will be passed as an argument of the mysql command.

SELECT g.`name`, COALESCE(SUM(r.`rate`), 0) AS rating
FROM `tv_genres` AS g
LEFT JOIN `tv_show_genres` AS sg ON g.`id` = sg.`genre_id`
LEFT JOIN `tv_shows` AS s ON sg.`show_id` = s.`id`
LEFT JOIN `tv_show_ratings` AS r ON s.`id` = r.`show_id`
GROUP BY g.`id`
ORDER BY rating DESC, g.`name`;
