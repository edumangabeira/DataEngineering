-- 11.1

SELECT a.primary_poc, b.channel, a.name
FROM accounts a
JOIN web_events B
ON b.account_id = a.id
WHERE a.name LIKE 'Walmart';


-- 11.2

SELECT a.name AS region_name, b.name AS sales_rep_name, c.name AS account_name
FROM accounts c
JOIN sales_reps b
ON c.sales_rep_id = b.id
JOIN region a
ON b.region_id = a.id
ORDER BY c.name;

-- 11.3

SELECT
a.name AS region_name,
c.name AS account_name,
d.total_amt_usd/(d.total+0.01) AS unit_price
FROM orders d
JOIN accounts c
ON c.id = d.account_id
JOIN sales_reps b
ON c.sales_rep_id = b.id
JOIN region a;

-- 19.1

SELECT a.name AS region_name,
b.name AS sales_rep_name,
c.name AS account_name
FROM region a
JOIN sales_reps b
ON b.region_id = a.id
AND a.name = 'Midwest'
JOIN accounts c
ON c.sales_rep_id = b.id
ORDER BY c.name;

-- 19.2

SELECT a.name AS region_name,
b.name AS sales_rep_name,
c.name AS account_name
FROM region a
JOIN sales_reps b
ON b.region_id = a.id
AND a.name = 'Midwest'
AND b.name LIKE 'S%'
JOIN accounts c
ON c.sales_rep_id = b.id
ORDER BY c.name;

-- 19.3

SELECT a.name AS region_name,
b.name AS sales_rep_name,
c.name AS account_name
FROM region a
JOIN sales_reps b
ON b.region_id = a.id
AND a.name = 'Midwest'
AND b.name LIKE '%K'
JOIN accounts c
ON c.sales_rep_id = b.id
ORDER BY c.name;

-- 19.4

SELECT
d.name region_name,
b.name account_name,
(a.total_amt_usd/a.total+0.01) AS unit_price
FROM orders a
JOIN accounts b
ON a.account_id = b.id
AND standard_qty > 100
JOIN sales_reps c
ON b.sales_rep_id = c.id
JOIN region d
ON c.region_id = d.id;

-- 19.5

SELECT
d.name region_name,
b.name account_name,
(a.total_amt_usd/a.total+0.01) AS unit_price
FROM orders a
JOIN accounts b
ON a.account_id = b.id
AND standard_qty > 100
AND poster_qty > 50
JOIN sales_reps c
ON b.sales_rep_id = c.id
JOIN region d
ON c.region_id = d.id
ORDER BY unit_price

-- 19.6

SELECT
d.name region_name,
b.name account_name,
(a.total_amt_usd/a.total+0.01) AS unit_price
FROM orders a
JOIN accounts b
ON a.account_id = b.id
AND standard_qty > 100
AND poster_qty > 50
JOIN sales_reps c
ON b.sales_rep_id = c.id
JOIN region d
ON c.region_id = d.id
ORDER BY unit_price DESC

-- 19.7
SELECT DISTINCT
b.channel,
a.name AS account_name
FROM accounts a
JOIN web_events b
ON b.account_id = a.id
WHERE b.account_id = 1001

-- 19.8

SELECT
a.occurred_at,
b.name AS account_name,
a.total,
a.total_amt_usd
FROM orders a
JOIN accounts b
ON a.account_id = b.id
WHERE occurred_at >= '01-01-2015'
AND occurred_at <= '12-31-2015'
-- aqui eu poderia ter usado a cláusula BETWEEN, fica bem mais fácil de ler.
