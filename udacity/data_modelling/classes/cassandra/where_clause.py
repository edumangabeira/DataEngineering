import cassandra

from cassandra.cluster import Cluster
try:
    cluster = Cluster(['127.0.0.1'])  # If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)

try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS udacity
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
                    )

except Exception as e:
    print(e)

try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)

query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (year, artist_name, album_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

query = "INSERT INTO music_library (year, artist_name, album_name, city)"
query = query + " VALUES (%s, %s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Let it Be", "Liverpool"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul", "Oxford"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "The Who", "My Generation", "London"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1966, "The Monkees", "The Monkees", "Los Angeles"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1970, "The Carpenters", "Close To You", "San Diego"))
except Exception as e:
    print(e)

# Give me every album in my music library that was released in a 1965 year
query = "select * from music_library where year = 1965"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)

# Give me the album that is in my music library that was released in 1965 by "The Beatles"
query = "select * from music_library where year = 1965 AND artist_name = 'The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)

# Give me all the albums released in a given year that was made in London
query = "select * from music_library where year = 1965 AND city = 'London' ALLOW FILTERING"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)

# Give me the city that the album "Rubber Soul" was recorded
query = "select * from music_library where year = 1965 AND artist_name = 'The Beatles' AND album_name = 'Rubber Soul'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.city)

query = "drop table if exists music_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

session.shutdown()
cluster.shutdown()
