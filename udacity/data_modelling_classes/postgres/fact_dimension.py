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

try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions(customer_id int, \
    store_id int, spent float)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)


try:
    cur.execute("INSERT INTO transactions(customer_id, store_id, spent) \
    VALUES(%s, %s, %s)", (1, 1, 20.50))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
try:
    cur.execute("INSERT INTO transactions(customer_id, store_id, spent) \
    VALUES(%s, %s, %s)", (2, 1, 35.21))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id int, \
    name text, rewards boolean)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO customer(id, name, rewards) \
    VALUES(%s, %s, %s)", (1, 'Amanda', 'y'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO customer(id, name, rewards) \
    VALUES(%s, %s, %s)", (2, 'Toby', 'n'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS store(id int, \
    state text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO store(id, state) \
    VALUES(%s, %s)", (1, 'CA'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
try:
    cur.execute("INSERT INTO store(id, state) \
    VALUES(%s, %s)", (2, 'WA'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS items_purchased(customer_id int, \
    item_num int, name text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("INSERT INTO items_purchased(customer_id, item_num, name) \
    VALUES(%s, %s, %s)", (1, 1, 'Rubber Soul'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("INSERT INTO items_purchased(customer_id, item_num, name) \
    VALUES(%s, %s, %s)", (2, 3, 'Let it Be'))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT b.name as customer, a.store_id as store \
    , d.state as state, c.name as product, b.rewards \
    FROM transactions a JOIN customer b \
    ON (a.customer_id = b.id AND a.spent > 30) \
    JOIN items_purchased c \
    ON c.customer_id = a.customer_id \
    JOIN store d \
    ON d.id = a.store_id")


except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("SELECT customer_id, spent FROM transactions \
    WHERE customer_id = 2")


except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

try:
    cur.execute("DROP TABLE transactions")

except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

try:
    cur.execute("DROP TABLE customer")

except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

try:
    cur.execute("DROP TABLE store")

except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)


try:
    cur.execute("DROP TABLE items_purchased")

except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

cur.close()
conn.close()
