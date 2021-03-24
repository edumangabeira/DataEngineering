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
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (artist_name))"
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

query = "select * from music_library WHERE artist_name = 'The Beatles' ALLOW FILTERING"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)


query = "CREATE TABLE IF NOT EXISTS album_library "
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (artist_name, album_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

# You can opt to change the sequence of columns to match your composite key. \
# Make sure to match the values in the INSERT statement

query = "INSERT INTO album_library (year, artist_name, album_name, city)"
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


query = "select * from album_library WHERE artist_name = 'The Beatles' ALLOW FILTERING"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)

query = "DROP TABLE IF EXISTS music_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

query = "DROP TABLE IF EXISTS album_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

session.shutdown()
cluster.shutdown()
