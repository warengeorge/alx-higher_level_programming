-- A script that lists all the cities of California
-- in the database hbtn_0d_usa.

SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
    );
