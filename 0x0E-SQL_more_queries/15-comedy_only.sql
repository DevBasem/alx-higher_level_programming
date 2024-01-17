-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
SELECT s.`title`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS gs
        ON s.`id` = gs.`show_id`
        INNER JOIN `tv_genres` AS g
        ON gs.`genre_id` = g.`id`
 WHERE g.`name` = 'Comedy'
 ORDER BY s.`title`;
