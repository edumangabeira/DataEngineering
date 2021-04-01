!PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila_star
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila_star -f Data/pagila-star.sql

import sql
%load_ext sql

DB_ENDPOINT = "127.0.0.1"
DB = 'pagila_star'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_PORT = '5432'

# postgresql://username:password@host:port/database
conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

print(conn_string)
%sql $conn_string


# total revenue

%%sql
SELECT SUM(sales_amount) as revenue
FROM factsales

# sales by country

%%sql
SELECT b.country as country, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimstore b
ON a.store_key = b.store_key
GROUP BY country
LIMIT 5

# sales by month

%%sql
SELECT c.month as month, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate c
ON a.date_key = c.date_key
GROUP BY month
LIMIT 5

# sales by month and country

%%sql
SELECT c.month as month, b.country as country, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimstore b
ON a.store_key = b.store_key
JOIN dimdate c
ON a.date_key = c.date_key
GROUP BY (month, country)
ORDER BY month, country, revenue desc
LIMIT 5


# revenue total, by month, by country, by month & country all in one shot

%%sql
SELECT c.month as month, b.country as country, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate c
ON a.date_key = c.date_key
JOIN dimstore b
ON a.store_key = b.store_key
GROUP BY GROUPING SETS ((), month, country, (month, country))


# CUBE - does the same as above

%%sql
SELECT c.month as month, b.country as country, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate c
ON a.date_key = c.date_key
JOIN dimstore b
ON a.store_key = b.store_key
GROUP BY cube(month, country)




