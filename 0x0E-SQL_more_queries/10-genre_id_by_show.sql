-- Lists all TV shows from the hbtn_0d_tvshows database that have at least one linked genre.
-- Each record displays the TV show title and corresponding genre ID.
-- Results are sorted in ascending order by TV show title and genre ID.

SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
