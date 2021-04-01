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

# SLICING

%%time
%%sql

SELECT b.day as day, c.rating as rating, d.city as city, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate b
ON a.date_key = b.date_key
JOIN dimmovie c
ON a.movie_key = c.movie_key
JOIN dimcustomer d
ON a.customer_key = d.customer_key
WHERE c.rating = 'PG-13'
GROUP BY day, rating, city
ORDER BY revenue DESC
LIMIT 20;

# DICING

%%time
%%sql

SELECT b.day as day, c.rating as rating, d.city as city, SUM(a.sales_amount) as revenue
FROM factsales a
JOIN dimdate b
ON a.date_key = b.date_key
JOIN dimmovie c
ON a.movie_key = c.movie_key
JOIN dimcustomer d
ON a.customer_key = d.customer_key
WHERE (c.rating = 'PG-13' OR c.rating = 'PG')
AND (d.city = 'Bellevue' OR d.city = 'Lancaster')
AND (b.day = 1 OR b.day = 15 OR b.day = 30)
GROUP BY day, rating, city
ORDER BY revenue DESC;


