-- A script that lists all cities in the database hbtn_0d_usa.
-- Use of join to display specific data

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id;
