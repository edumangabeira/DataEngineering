# DROP TABLES

songplay_table_drop = "DROP TABLE songplay"
user_table_drop = "DROP TABLE user"
song_table_drop = "DROP TABLE song"
artist_table_drop = "DROP TABLE artist"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplay(songplay_id text, \
    start_time text, user_id text, level text, song_id text, artist_id text, \
    session_id text, location text, user_agent text, PRIMARY KEY(songplay_id);"

user_table_create = "CREATE TABLE IF NOT EXISTS user(user_id text, first_name text, \
    last_name text, gender varchar(1), level text, PRIMARY KEY(user_id));"

song_table_create = "CREATE TABLE IF NOT EXISTS song(song_id text, title text, \
    artist_id text, year int, duration float, PRIMARY_KEY(song_id));"

artist_table_create = "CREATE TABLE IF NOT EXISTS artist(artist_id text, name text, \
    location text, latitude float, longitude float, PRIMARY_KEY(artist_id));"

time_table_create = "CREATE TABLE IF NOT EXISTS time(start_time text, hour text, \
    day int, week int, month int, year int, weekday text);"

# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplay(songplay_id, start_time, user_id, level, \
                                               song_id, artist_id, session_id, location, \
                                                user_agent) \
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

user_table_insert = "INSERT INTO user(user_id, first_name, last_name, gender, level) \
    VALUES(%s, %s, %s, %s, %s)"

song_table_insert = "INSERT INTO song(song_id, title, artist_id, year, duration) \
    VALUES(%s, %s, %s, %s, %s)"


artist_table_insert = "INSERT INTO artist(artist_id, name, location, \
    latitude, longitude) \
    VALUES(%s, %s, %s, %s, %s)"


time_table_insert = "INSERT INTO time(start_time, hour, day, week, \
    month, year, weekday) \
    VALUES(%s, %s, %s, %s, %s, %s, %s)"


# FIND SONGS

song_select = "SELECT song_id, title, artist_id, year, duration FROM song"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
