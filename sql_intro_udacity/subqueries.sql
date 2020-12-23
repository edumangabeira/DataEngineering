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