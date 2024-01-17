-- Lists all shows in hbtn_0d_tvshows without a genre linked.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        LEFT JOIN `tv_show_genres` AS g
        ON s.`id` = g.`show_id`
 WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;
