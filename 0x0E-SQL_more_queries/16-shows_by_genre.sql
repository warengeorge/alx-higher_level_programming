-- A  script that  lists all shows, and all genres linked to
-- that show, from the hbtn_0d_tvshows database.
-- using join to dsplay data and order based on title and name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
