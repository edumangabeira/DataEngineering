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


query = "CREATE TABLE IF NOT EXISTS album_library"
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (artist_name, year, album_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

# You can opt to change the sequence of columns to match your composite key. \
# If you do, make sure to match the values in the INSERT statement

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
    session.execute(query, (1964, "The Beatles", "Beatles For Sale", "London"))
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

query = "select * from album_library WHERE album_name='Close To You' ALLOW FILTERING"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.artist_name, row.album_name, row.city, row.year)

query = "drop table if exists album_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

session.shutdown()
cluster.shutdown()
