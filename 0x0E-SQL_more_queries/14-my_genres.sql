-- Lists all genres of the show Dexter from hbtn_0d_tvshows.
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name
SELECT g.`name`
  FROM `tv_genres` AS g
        INNER JOIN `tv_show_genres` AS gs
        ON g.`id` = gs.`genre_id`
        INNER JOIN `tv_shows` AS s
        ON gs.`show_id` = s.`id`
 WHERE s.`title` = 'Dexter'
 GROUP BY g.`id`
 ORDER BY g.`name`;
