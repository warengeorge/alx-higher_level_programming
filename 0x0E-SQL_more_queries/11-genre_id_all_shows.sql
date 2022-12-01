-- A script that lists all shows in the database hbtn_0d_tvshows.
-- using join to dsplay data and order based on title and genre id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
