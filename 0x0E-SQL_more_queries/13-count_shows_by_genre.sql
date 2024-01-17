-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results are sorted in descending order by the number of shows linked
SELECT g.`name` AS genre, COUNT(s.`id`) AS number_of_shows
  FROM `tv_genres` AS g
        INNER JOIN `tv_show_genres` AS gs
        ON g.`id` = gs.`genre_id`
        INNER JOIN `tv_shows` AS s
        ON gs.`show_id` = s.`id`
 GROUP BY g.`id`
 ORDER BY number_of_shows DESC, genre;
