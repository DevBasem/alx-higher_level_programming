-- Lists all shows without the genre Comedy in the hbtn_0d_tvshows database.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title.
-- You can use a maximum of two SELECT statements.
-- The database name will be passed as an argument of the mysql command.

SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
WHERE t.`id` NOT IN (
    SELECT s.`show_id`
    FROM `tv_show_genres` AS s
    JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
    WHERE g.`name` = 'Comedy'
)
ORDER BY t.`title`;
