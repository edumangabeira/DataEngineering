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

# ROLL UP

%%time
%%sql
SELECT b.day as day, c.rating as rating, d.country as country, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate b
ON a.date_key = b.date_key
JOIN dimmovie c
ON a.movie_key = c.movie_key
JOIN dimcustomer d
ON a.customer_key = d.customer_key
GROUP BY day, rating, country
ORDER BY revenue DESC
LIMIT 20;


# DRILL DOWN

%%time
%%sql
SELECT b.day as day, c.rating as rating, d.district as district, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate b
ON a.date_key = b.date_key
JOIN dimmovie c
ON a.movie_key = c.movie_key
JOIN dimcustomer d
ON a.customer_key = d.customer_key
GROUP BY day, rating, district
ORDER BY revenue DESC
LIMIT 20;


