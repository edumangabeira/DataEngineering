-- 7.1

SELECT SUM(poster_qty) as poster_qty_sum
FROM orders;

-- 7.2

SELECT SUM(poster_qty) as poster_qty_sum
FROM orders;

-- 7.3

SELECT SUM(total_amt_usd) as total_amt_usd_sum
FROM orders;

-- 7.4

SELECT standard_amt_usd + gloss_amt_usd AS total_amount_spent
FROM orders;

-- 7.5

SELECT SUM(standard_amt_usd) / SUM(standard_qty)
FROM orders;

-- 11.1

SELECT MIN(occurred_at)
FROM orders;

-- 11.2

SELECT occurred_at
FROM orders
ORDER BY occurred_at
LIMIT 1;

-- 11.3

SELECT MAX(occurred_at)
FROM web_events;

-- 11.4

SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;

-- 11.5

SELECT
AVG(standard_amt_usd) AS avg_std_usd,
AVG(gloss_amt_usd) AS avg_gloss_usd,
AVG(poster_amt_usd) AS avg_poster_usd,
AVG(standard_qty) AS avg_std_qty,
AVG(gloss_qty) AS avg_gloss_qty,
AVG(poster_qty) AS avg_poster_qty
FROM orders;

-- 11.6

SELECT
COUNT(total_amt_usd)/2.0
FROM orders;
-- chequei se o número de linhas é ímpar. Como não é,
-- decidi encontrar os dois valores do meio, somar e dividir por dois.

SELECT (a.total_amt_usd + b.total_amt_usd)/2
FROM orders a
JOIN orders b
ON a.id = b.id
ORDER BY a.total_amt_usd
-- Fiz  a = (q)/2 e b = (q/2) + 1.
-- Não consegui pensar num jeito de capturar as posições.


-- 14.1

SELECT
MIN(a.occurred_at) AS min,
b.name
FROM accounts b
JOIN orders a
ON a.account_id = b.id
GROUP BY b.name
ORDER BY min
LIMIT 1;

-- não precisava agrupar.

-- 14.2

SELECT
SUM(a.total_amt_usd) AS total,
b.name
FROM accounts b
JOIN orders a
ON a.account_id = b.id
GROUP BY b.name;

-- 14.3

SELECT
MAX(a.occurred_at) AS latest,
a.channel,
b.name
FROM web_events a
JOIN accounts b
ON a.account_id = b.id
GROUP BY a.channel,  b.name
ORDER BY latest DESC
LIMIT 1;
-- não precisava agrupar.

-- 14.4

SELECT
COUNT(channel) AS num_channel,
channel
FROM web_events
GROUP BY channel;

-- 14.5

SELECT
MIN(a.occurred_at) AS earliest,
b.primary_poc
FROM web_events a
JOIN accounts b
ON a.account_id = b.id
GROUP BY b.primary_poc
ORDER BY earliest
LIMIT 1;
-- Não precisava agrupar

-- 14.6

SELECT
b.name,
MIN(c.total_amt_usd) as min_order
FROM orders c
JOIN accounts b
ON c.account_id = b.id
GROUP BY b.name
ORDER BY min_order;

-- 14.7

SELECT
COUNT(d.name) as sales_rep_qty,
e.name
FROM sales_reps d
JOIN region e
ON d.region_id = e.id
GROUP BY e.name
ORDER BY sales_rep_qty;


-- 17.1

SELECT
a.name,
AVG(b.standard_qty) AS avg_std_qty,
AVG(b.gloss_qty) AS avg_gloss_qty,
AVG(b.poster_qty) AS avg_poster_qty
FROM orders b
JOIN accounts a
ON b.account_id = a.id
GROUP BY a.name;

-- 17.2

SELECT
a.name,
AVG(b.standard_amt_usd) AS avg_std_amt_usd,
AVG(b.gloss_amt_usd) AS avg_gloss_amt_usd,
AVG(b.poster_amt_usd) AS avg_poster_amt_usd
FROM orders b
JOIN accounts a
ON b.account_id = a.id
GROUP BY a.name;

-- 17.3

SELECT
COUNT(a.channel) as channel_count,
a.channel,
c.name as sales_rep_name
FROM web_events a
JOIN accounts b
ON a.account_id = b.id
JOIN sales_reps c
ON b.sales_rep_id = c.id
GROUP BY a.channel, sales_rep_name
ORDER BY channel_count DESC;

-- 17.4

SELECT
COUNT(a.channel) as channel_count,
a.channel,
d.name as region_name
FROM web_events a
JOIN accounts b
ON a.account_id = b.id
JOIN sales_reps c
ON b.sales_rep_id = c.id
JOIN region d
ON c.region_id = d.id
GROUP BY a.channel, region_name
ORDER BY channel_count DESC;

-- 20.1

SELECT a.name AS account, c.name AS region
FROM accounts a
JOIN sales_reps b
ON a.sales_rep_id = b.id
JOIN region c
ON b.region_id = c.id;

SELECT DISTINCT id, name
FROM accounts;
-- 20.2

SELECT a.name AS account, b.name AS sales_rep, COUNT(b.name) AS count_sales_rep
FROM accounts a
JOIN sales_reps b
ON a.sales_rep_id = b.id
GROUP BY account, sales_rep
ORDER BY count_sales_rep DESC;

SELECT DISTINCT id, name
FROM sales_reps;

-- 23.1

SELECT b.name AS sales_rep,
COUNT(a.name) AS accounts
FROM accounts a
JOIN sales_reps b
ON a.sales_rep_id = b.id
GROUP BY sales_rep
HAVING COUNT(a.name) > 5

--23.2

SELECT COUNT(c.id) AS orders,
a.id AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
HAVING COUNT(c.id) > 20
ORDER BY orders

--23.3

SELECT COUNT(c.id) AS orders,
a.name AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
HAVING COUNT(c.id) > 20
ORDER BY orders DESC
LIMIT 1

--23.4

SELECT SUM(c.total_amt_usd) AS orders_total_usd,
a.name AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
HAVING SUM(c.total_amt_usd) > 30000


--23.5

SELECT SUM(c.total_amt_usd) AS orders_total_usd,
a.name AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
HAVING SUM(c.total_amt_usd) < 1000

--23.6

SELECT SUM(c.total_amt_usd) AS orders_total_usd,
a.name AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
ORDER BY orders_total_usd DESC
LIMIT 1

--23.7

SELECT SUM(c.total_amt_usd) AS orders_total_usd,
a.name AS accounts
FROM accounts a
JOIN orders c
ON a.id = c.account_id
GROUP BY accounts
ORDER BY orders_total_usd
LIMIT 1

--23.8

SELECT COUNT(b.channel),
a.name
FROM web_events b
JOIN accounts a
ON b.account_id = a.id
AND b.channel LIKE 'facebook'
GROUP BY a.name
HAVING COUNT(b.channel) > 6

--23.9

SELECT COUNT(b.channel) AS times_contact,
a.name
FROM web_events b
JOIN accounts a
ON b.account_id = a.id
AND b.channel LIKE 'facebook'
GROUP BY a.name
ORDER BY times_contact DESC
LIMIT 1

--23.10

SELECT COUNT(b.channel) AS times_contact,
a.name,
b.channel
FROM web_events b
JOIN accounts a
ON b.account_id = a.id
GROUP BY a.name, b.channel
ORDER BY times_contact DESC
LIMIT 15


-- 27.1

SELECT DATE_TRUNC('year',occurred_at), SUM(total_amt_usd) as total
FROM orders
GROUP BY DATE_TRUNC('year', occurred_at)
ORDER BY DATE_TRUNC('year', occurred_at)

-- Entre 2013 e 2016 parece haver crescimento anual nas vendas, mas em 2017 há uma queda brusca.
-- Os dados de 2013 e 2017 não estão completos.


-- 31.5

SELECT
COUNT(a.id) as count_orders,
b.name as sales_rep,
CASE WHEN COUNT(a.id) > 200 THEN 'top'
     ELSE 'not top' END AS sales_level
FROM orders a
JOIN accounts c
ON a.account_id = c.id
JOIN sales_reps b
ON c.sales_rep_id = b.id
GROUP BY sales_rep
ORDER BY count_orders DESC
