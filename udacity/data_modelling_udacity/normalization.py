import psycopg2

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)
conn.set_session(autocommit=True)

# sem normalização
try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_store (transaction_id int, customer_name text, \
    cashier_name text, year int, albums_purchased text[])")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO music_store (transaction_id, customer_name, \
    cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (1, 'Amanda', 'Sam', 2000, ['Rubber Soul', 'Let it Be']))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store (transaction_id, customer_name, \
    cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (2, 'Toby', 'Sam', 2018, ['My Generation']))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store (transaction_id, customer_name, \
    cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (3, 'Max', 'Bob', 2000, ['Meet the Beatles', 'Help!']))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


try:
    cur.execute("SELECT * FROM music_store;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()


# 1NF

try:
    cur.execute("CREATE TABLE IF NOT EXISTS music_store2 (transaction_id int, customer_name text, \
    cashier_name text, year int, album_purchased text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, \
    cashier_name, year, album_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (1, 'Amanda', 'Sam', 2000, 'Rubber Soul'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, \
    cashier_name, year, album_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (2, 'Amanda', 'Sam', 2000, 'Let it Be'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, \
    cashier_name, year, album_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (3, 'Toby', 'Sam', 2000, 'My Generation'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, \
    cashier_name, year, album_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (4, 'Max', 'Bob', 2018, 'Meet the Beatles'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO music_store2 (transaction_id, customer_name, \
    cashier_name, year, album_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
                (5, 'Max', 'Bob', 2018, 'Help!'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


try:
    cur.execute("SELECT * FROM music_store2;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# 2NF

try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (id int, customer text, \
    cashier text, year int, PRIMARY KEY (id));")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (id int, transaction_id int, \
    name text, PRIMARY KEY(id), FOREIGN KEY(transaction_id) REFERENCES transactions(id));")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier, year) \
                 VALUES (%s, %s, %s, %s)",
                (1, 'Amanda', 'Sam', 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier, year) \
                 VALUES (%s, %s, %s, %s)",
                (2, 'Toby', 'Sam', 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions (id, customer, cashier, year) \
                 VALUES (%s, %s, %s, %s)",
                (3, 'Max', 'Bob', 2018))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (1, 1, 'Rubber Soul'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (2, 1, 'Let it Be'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (3, 2, 'My Generation'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (4, 3, 'Meet the Beatles'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO albums_sold (id, transaction_id, name) \
                 VALUES (%s, %s, %s)",
                (5, 3, 'Help!'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

print("Table: transactions\n")
try:
    cur.execute("SELECT * FROM transactions;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: albums_sold\n")
try:
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)
row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# JOIN 2NF

try:
    cur.execute("SELECT * FROM albums_sold a JOIN transactions t ON t.id = a.transaction_id;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# 3NF

try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 (id int , customer text, cashier_id int, year int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id int, name text);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (1, 'Amanda', 1, 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (2, 'Toby', 1, 2000))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO transactions2 (id, customer, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
                (3, 'Max', 2, 2018))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO employees (id, name) \
                 VALUES (%s, %s)",
                (1, 'Sam'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO employees (id, name) \
                 VALUES (%s, %s)",
                (2, 'Bob'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

print("Table: transactions2\n")
try:
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: albums_sold\n")
try:
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: employees\n")
try:
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

#  JOIN 3NF

try:
    cur.execute("SELECT * FROM (albums_sold a JOIN transactions2 b ON \
                               a.transaction_id = b.id) JOIN \
                               employees c ON c.id = b.cashier_id;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("DROP table music_store")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table music_store2")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table albums_sold")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table employees")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table transactions")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table transactions2")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

cur.close()
conn.close()
