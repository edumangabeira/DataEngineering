# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, \
    start_time text, user_id text, level text, song_id text, artist_id text, \
    session_id int, location text, user_agent text);"

user_table_create = "CREATE TABLE IF NOT EXISTS users(user_id text PRIMARY KEY , first_name text, \
    last_name text, gender varchar(1), level text);"

song_table_create = "CREATE TABLE IF NOT EXISTS songs(song_id text PRIMARY KEY, title text, \
    artist_id text, year int, duration float);"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists(artist_id text PRIMARY KEY , name text, \
    location text, latitude float, longitude float);"

time_table_create = "CREATE TABLE IF NOT EXISTS time(start_time text PRIMARY KEY, hour int, \
    day int, week int, month int, year int, weekday text);"

# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplays(start_time, user_id, level, \
    song_id, artist_id, session_id, location, user_agent) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

user_table_insert = "INSERT INTO users(user_id, first_name, last_name, gender, level) \
    VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING"

song_table_insert = "INSERT INTO songs(song_id, title, artist_id, year, duration) \
    VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING"


artist_table_insert = "INSERT INTO artists(artist_id, name, location, \
    latitude, longitude) \
    VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING"


time_table_insert = "INSERT INTO time(start_time, hour, day, week, \
    month, year, weekday) \
    VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING"


# FIND SONGS

song_select = ("""
SELECT b.song_id, a.artist_id
FROM artists a
JOIN songs b
ON a.artist_id = b.artist_id
WHERE b.title = %s
AND a.name = %s
AND b.duration = %s;
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]