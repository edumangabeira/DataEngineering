# Create the pagila db and fill it with data

!PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-schema.sql
!PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-data.sql

# Connect to the newly created d
%load_ext sql

DB_ENDPOINT = "127.0.0.1"
DB = 'pagila'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_PORT = '5432'

# postgresql://username:password@host:port/database
conn_string = "postgresql://{}:{}@{}:{}/{}" \
                        .format(DB_USER, DB_PASSWORD, DB_ENDPOINT, DB_PORT, DB)

print(conn_string)

%sql $conn_string

# check data size
nStores = %sql select count(*) from store;
nFilms = %sql select count(*) from film;
nCustomers = %sql select count(*) from customer;
nRentals = %sql select count(*) from rental;
nPayment = %sql select count(*) from payment;
nStaff = %sql select count(*) from staff;
nCity = %sql select count(*) from city;
nCountry = %sql select count(*) from country;

print("nFilms\t\t=", nFilms[0][0])
print("nCustomers\t=", nCustomers[0][0])
print("nRentals\t=", nRentals[0][0])
print("nPayment\t=", nPayment[0][0])
print("nStaff\t\t=", nStaff[0][0])
print("nStores\t\t=", nStores[0][0])
print("nCities\t\t=", nCity[0][0])
print("nCountry\t\t=", nCountry[0][0])

# time period

%%sql 
select min(payment_date) as start, max(payment_date) as end from payment;


# where do events occur?
query = """select district, COUNT(*) as n \
FROM address \
GROUP BY district 
ORDER by n DESC \
LIMIT 10 """

%sql $query

%%sql
select film_id, title, release_year, rental_rate, rating  from film limit 5;

%%sql
select * from payment limit 5;


%%sql
select * from inventory limit 5;

%%sql
SELECT f.title, p.amount, p.payment_date, p.customer_id                                            
FROM payment p
JOIN rental r    ON ( p.rental_id = r.rental_id )
JOIN inventory i ON ( r.inventory_id = i.inventory_id )
JOIN film f ON ( i.film_id = f.film_id)
limit 5;


# top grossing cities
%%sql
SELECT d.city as city, SUM(a.amount) as revenue                          
FROM payment a
JOIN customer b  ON a.customer_id = b.customer_id
JOIN address c ON b.address_id = c.address_id
JOIN city d ON d.city_id = c.city_id
GROUP BY city
ORDER BY revenue DESC
LIMIT 10;



'''
Queries got more complicated, so let's denormalize 
the database  and set fact and dimension tables.
'''

################ NEXT STEPS


%%sql
CREATE TABLE dimDate
(
    date_key   SERIAL   PRIMARY KEY,
    date       DATE     NOT NULL,
    year       SMALLINT NOT NULL,
    quarter    SMALLINT NOT NULL,
    month      SMALLINT NOT NULL,
    day        SMALLINT NOT NULL,
    week       SMALLINT NOT NULL,
    is_weekend BOOLEAN  NOT NULL
);

%%sql
CREATE TABLE dimCustomer
(
  customer_key SERIAL PRIMARY KEY,
  customer_id  smallint NOT NULL,
  first_name   varchar(45) NOT NULL,
  last_name    varchar(45) NOT NULL,
  email        varchar(50),
  address      varchar(50) NOT NULL,
  address2     varchar(50),
  district     varchar(20) NOT NULL,
  city         varchar(50) NOT NULL,
  country      varchar(50) NOT NULL,
  postal_code  varchar(10),
  phone        varchar(20) NOT NULL,
  active       smallint NOT NULL,
  create_date  timestamp NOT NULL,
  start_date   date NOT NULL,
  end_date     date NOT NULL
);

CREATE TABLE dimMovie
(
  movie_key          SERIAL PRIMARY KEY,
  film_id            smallint NOT NULL,
  title              varchar(255) NOT NULL,
  description        text,
  release_year       year,
  language           varchar(20) NOT NULL,
  original_language  varchar(20),
  rental_duration    smallint NOT NULL,
  length             smallint NOT NULL,
  rating             varchar(5) NOT NULL,
  special_features   varchar(60) NOT NULL
);
CREATE TABLE dimStore
(
  store_key           SERIAL PRIMARY KEY,
  store_id            smallint NOT NULL,
  address             varchar(50) NOT NULL,
  address2            varchar(50),
  district            varchar(20) NOT NULL,
  city                varchar(50) NOT NULL,
  country             varchar(50) NOT NULL,
  postal_code         varchar(10),
  manager_first_name  varchar(45) NOT NULL,
  manager_last_name   varchar(45) NOT NULL,
  start_date          date NOT NULL,
  end_date            date NOT NULL
);


%%sql
CREATE TABLE factSales
(
    sales_key    SERIAL PRIMARY KEY,
    date_key     INT REFERENCES dimDate (date_key),
    customer_key INT REFERENCES dimCustomer (customer_key),
    movie_key    INT REFERENCES dimMovie (movie_key),
    store_key    INT REFERENCES dimStore (store_key),
    sales_amount numeric NOT NULL

);









