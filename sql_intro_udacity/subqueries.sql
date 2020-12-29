-- 3.1

SELECT DATE_TRUNC('day', occurred_at) AS day,
channel,
COUNT(*) as event_count
FROM web_events
GROUP BY day, channel

-- 3.2

SELECT DATE_TRUNC('day', occurred_at) AS day,
channel,
COUNT(*) as event_count
FROM web_events
GROUP BY day, channel
ORDER BY event_count DESC

-- 3.3

SELECT * FROM
(SELECT DATE_TRUNC('day', occurred_at) AS day,
channel,
COUNT(*) as event_count
FROM web_events
GROUP BY day, channel
ORDER BY event_count DESC) sub


-- 3.4

SELECT AVG(event_count), channel
FROM(SELECT DATE_TRUNC('day', occurred_at) AS day,
	channel,
	COUNT(*) as event_count
	FROM web_events
	GROUP BY day, channel
	ORDER BY event_count DESC) sub
GROUP BY 2
ORDER BY 1 DESC



-- 7.1

SELECT MIN(DATE_TRUNC('month', occurred_at))
FROM orders


-- 7.3

SELECT AVG(standard_qty) AS standard,
AVG(gloss_qty) AS gloss,
AVG(poster_qty) AS poster
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
	(SELECT MIN(DATE_TRUNC('month', occurred_at))
	FROM orders)

-- 7.4

SELECT AVG(standard_qty) AS standard,
AVG(gloss_qty) AS gloss,
AVG(poster_qty) AS poster,
SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
	(SELECT MIN(DATE_TRUNC('month', occurred_at))
	FROM orders)

-- 9.1

SELECT sub3.sales_rep, sub3.total_usd, sub3.region
FROM
(SELECT region,
MAX(total_usd) as total_amt
FROM
(SELECT c.name as sales_rep,
d.name as region,
SUM(a.total_amt_usd) as total_usd
FROM orders a
JOIN accounts b
ON b.id = a.account_id
JOIN sales_reps c
ON c.id = b.sales_rep_id
JOIN region d
on d.id = c.region_id
GROUP BY 1,2) sub1
GROUP BY 1) sub2
JOIN
(SELECT c.name as sales_rep,
d.name as region,
SUM(a.total_amt_usd) as total_usd
FROM orders a
JOIN accounts b
ON b.id = a.account_id
JOIN sales_reps c
ON c.id = b.sales_rep_id
JOIN region d
on d.id = c.region_id
GROUP BY 1,2
ORDER BY 3 DESC) sub3
ON
sub3.region = sub2.region  AND sub3.total_usd = sub2.total_amt


-- 9.2

SELECT d.name as region,
COUNT(a.total) as total_orders
FROM
(SELECT
SUM(a.total_amt_usd) as total_usd
FROM orders a
JOIN accounts b
ON b.id = a.account_id
JOIN sales_reps c
ON c.id = b.sales_rep_id
JOIN region d
on d.id = c.region_id
ORDER BY 1 DESC
LIMIT 1)
GROUP BY 1;
