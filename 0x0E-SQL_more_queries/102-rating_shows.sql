-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum.
-- Results must be sorted in descending order by the rating.
-- You can use only one SELECT statement.
-- The database name will be passed as an argument of the mysql command.

SELECT t.`title`, COALESCE(SUM(r.`rate`), 0) AS rating
FROM `tv_shows` AS t
LEFT JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`
GROUP BY t.`id`
ORDER BY rating DESC, t.`title`;
