import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events(
    event_id        IDENTITY(0,1)  PRIMARY KEY,
    artist_name     TEXT,
    auth            TEXT,
    user_first_name TEXT,
    user_gender     TEXT,
    item_in_session INTEGER,
    user_last_name  TEXT,
    song_length     FLOAT, 
    user_level      TEXT,
    location        TEXT,
    method          TEXT,
    page            TEXT,
    registration    TEXT,
    session_id      INT,
    song_title      TEXT,
    status          INT,
    ts              TEXT,
    user_agent      TEXT,
    user_id         TEXT
    );
""")

staging_songs_table_create = ("""
CREATE TABLE staging_events(
    event_id        IDENTITY(0,1) PRIMARY KEY,
    artist_name     TEXT,
    auth            TEXT,
    user_first_name TEXT,
    user_gender     TEXT,
    item_in_session TEXT,
    user_last_name  TEXT,
    song_length     FLOAT, 
    user_level      TEXT,
    location        TEXT,
    method          TEXT,
    page            TEXT,
    registration    TEXT,
    session_id      INT,
    song_title      TEXT,
    status          INT,
    ts              TEXT,
    user_agent      TEXT,
    user_id         TEXT
    );
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
    songplay_id IDENTITY(0,1)  PRIMARY KEY,
    start_time  TEXT   NOT NULL,
    user_id     TEXT   NOT NULL,
    level       TEXT,
    song_id     TEXT,
    artist_id   TEXT,
    session_id  INT,
    location    TEXT,
    user_agent  TEXT
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
    user_id    TEXT        PRIMARY KEY,
    first_name TEXT,
    last_name  TEXT,
    gender     VARCHAR(1),
    level      TEXT
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
    song_id   TEXT  PRIMARY KEY,
    title     TEXT,
    artist_id TEXT,
    year      INT,
    duration  FLOAT
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT  PRIMARY KEY ,
    name      TEXT,
    location  TEXT,
    latitude  FLOAT,
    longitude FLOAT
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour       INT,
    day        INT,
    week       INT,
    month      INT,
    year       INT,
    weekday    TEXT
    );
""")


# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events
    FROM {}
    iam_role {}
    json {};
""").format(config['S3']['LOG_DATA'], config['IAM_ROLE']['ARN'], config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
    COPY staging_songs
    FROM {}
    iam_role {}
    json 'auto';
""").format(config['S3']['SONG_DATA'], config['IAM_ROLE']['ARN'])

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    SELECT events.start_time, events.user_id, events.level, songs.song_id, songs.artist_id, events.session_id, events.location, events.user_agent
    FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
          FROM staging_events
          WHERE page='NextSong') events
    LEFT JOIN staging_songs songs
    ON events.song = songs.title
    AND events.artist = songs.artist_name
    AND events.length = songs.duration
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    SELECT DISTINCT user_id, first_name, last_name, gender, level
    FROM staging_events
    WHERE page='NextSong'
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    SELECT DISTINCT song_id, title, artist_id, year, duration
    FROM staging_songs
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    SELECT DISTINCT artist_id, name, location, latitude, longitude
    FROM staging_songs
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    SELECT DISTINCT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, EXTRACT(hour from start_time), EXTRACT(day from start_time), EXTRACT(week from start_time), EXTRACT(month from start_time), EXTRACT(year from start_time), EXTRACT(dayofweek from start_time)
    FROM staging_events
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
