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



