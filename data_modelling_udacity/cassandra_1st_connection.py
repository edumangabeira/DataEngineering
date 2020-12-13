import cassandra


from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1'])
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

query = "CREATE TABLE IF NOT EXISTS SongLib"
query = query + "(song_title text, artist_name text, year int, album_name text, single boolean, PRIMARY KEY (year, song_title))"
try:
    session.execute(query)
except Exception as e:
    print(e)


query = "INSERT INTO SongLib(song_title, artist_name, year, album_name, single)" 
query = query + "VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, ("Across The Universe", "The Beatles", 1970, "Let It Be", False))
except Exception as e:
    print(e)
    
try:
    session.execute(query, ("Think For Yourself", "The Beatles", 1965, "Rubber Soul", False))
except Exception as e:
    print(e)

query = 'SELECT * FROM SongLib'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)

'''
Quando tentei usar mais de um filtro, mesmo que especificando um item em vez de percorrer
uma partição inteira, recebi um erro(quase um warning) dizendo que essa operação seria
muito custosa e por isso é desencorajada.

Correção: Descobri o motivo, eu modelei o banco para fazer consultas com 'year' e 'song_title'
e tentei fazer uma consulta com 'album_name', por isso deu errado.

https://stackoverflow.com/questions/38350656/cassandra-asks-for-allow-filtering-even-though-column-is-clustering-key
'''

query = "select year from SongLib WHERE year=1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year)


session.shutdown()
cluster.shutdown()