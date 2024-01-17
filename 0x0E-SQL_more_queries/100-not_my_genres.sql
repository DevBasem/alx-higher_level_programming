-- Lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different).
-- Each record displays: tv_genres.name.
-- Results are sorted in ascending order by the genre name.

-- Step 1: Select the genre IDs linked to the show Dexter
SELECT DISTINCT tg.`id`
FROM `tv_genres` tg
INNER JOIN `tv_show_genres` tsg ON tg.`id` = tsg.`genre_id`
INNER JOIN `tv_shows` ts ON tsg.`show_id` = ts.`id`
WHERE ts.`title` = 'Dexter';

-- Step 2: Select all genres not linked to the show Dexter
SELECT `name`
FROM `tv_genres`
WHERE `id` NOT IN (
    -- Subquery to get genre IDs linked to Dexter
    SELECT DISTINCT tg.`id`
    FROM `tv_genres` tg
    INNER JOIN `tv_show_genres` tsg ON tg.`id` = tsg.`genre_id`
    INNER JOIN `tv_shows` ts ON tsg.`show_id` = ts.`id`
    WHERE ts.`title` = 'Dexter'
)
ORDER BY `name`;
