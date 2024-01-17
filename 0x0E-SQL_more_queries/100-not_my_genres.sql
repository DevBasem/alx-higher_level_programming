-- Lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different).
-- Each record displays: tv_genres.name.
-- Results are sorted in ascending order by the genre name.

SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN (
    SELECT g2.`name`
    FROM `tv_genres` AS g2
    INNER JOIN `tv_show_genres` AS s2 ON g2.`id` = s2.`genre_id`
    INNER JOIN `tv_shows` AS t2 ON s2.`show_id` = t2.`id`
    WHERE t2.`title` = 'Dexter'
)
ORDER BY g.`name`;
