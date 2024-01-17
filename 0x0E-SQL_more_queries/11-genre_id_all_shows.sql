-- Lists all shows in hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
-- If a show doesn’t have a genre, display NULL.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        LEFT JOIN `tv_show_genres` AS g
        ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
