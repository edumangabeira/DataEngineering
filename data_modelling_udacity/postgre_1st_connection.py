import psycopg2

# connect
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
# cursor
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)
# autocommit
conn.set_session(autocommit=True)

# create db
try:
    cur.execute("create database hello_world")

except psycopg2.Error as e:
    print(e)

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=hello_world user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)


try:
    cur.execute("CREATE TABLE IF NOT EXISTS SongLib (song_title text, artist_name text, year numeric(4), album_name text, single boolean);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO SongLib (song_title, artist_name, year, album_name, single) \
                 VALUES (%s, %s, %s, %s, %s)",
                ("Across The Universe", "The Beatles", 1970, "Let it Be", False))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO SongLib (song_title, artist_name, year, album_name, single) \
                 VALUES (%s, %s, %s, %s, %s)",
                ("Think For Yourself", "The Beatles", 1965, "Rubber Soul", False))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT * FROM SongLib;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

cur.close()
conn.close()
