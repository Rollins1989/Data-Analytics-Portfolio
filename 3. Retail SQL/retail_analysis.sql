-- Retail Business Intelligence
-- Reusable SQL queries for the SQLite schema in retail_analytics.db.

-- 1. Revenue by category and year
SELECT
    p.category,
    strftime('%Y', o.order_date) AS year,
    ROUND(SUM(i.quantity * i.unit_price * (1 - i.discount)), 2) AS total_revenue
FROM order_items i
JOIN orders o ON i.order_id = o.order_id
JOIN products p ON i.product_id = p.product_id
WHERE o.status = 'Completed'
GROUP BY p.category, year
ORDER BY year, total_revenue DESC;

-- 2. Category year-over-year comparison
WITH yearly AS (
    SELECT
        p.category,
        strftime('%Y', o.order_date) AS year,
        SUM(i.quantity * i.unit_price * (1 - i.discount)) AS total_revenue
    FROM order_items i
    JOIN orders o ON i.order_id = o.order_id
    JOIN products p ON i.product_id = p.product_id
    WHERE o.status = 'Completed'
    GROUP BY p.category, year
)
SELECT
    category,
    year,
    ROUND(total_revenue, 2) AS total_revenue,
    ROUND(
        (total_revenue - LAG(total_revenue) OVER (PARTITION BY category ORDER BY year))
        * 100.0 / NULLIF(LAG(total_revenue) OVER (PARTITION BY category ORDER BY year), 0),
        1
    ) AS yoy_growth_pct
FROM yearly
ORDER BY category, year;

-- 3. Top customers by lifetime spend
SELECT
    c.customer_id,
    c.name,
    c.tier,
    c.city,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(i.quantity * i.unit_price * (1 - i.discount)), 2) AS total_spend,
    ROUND(AVG(i.quantity * i.unit_price * (1 - i.discount)), 2) AS avg_order_value,
    RANK() OVER (
        ORDER BY SUM(i.quantity * i.unit_price * (1 - i.discount)) DESC
    ) AS spend_rank
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items i ON o.order_id = i.order_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.name, c.tier, c.city
ORDER BY total_spend DESC
LIMIT 20;

-- 4. Product profitability
SELECT
    p.product_id,
    p.name AS product_name,
    p.category,
    SUM(i.quantity) AS units_sold,
    ROUND(SUM(i.quantity * i.unit_price * (1 - i.discount)), 2) AS revenue,
    ROUND(SUM(i.quantity * p.unit_cost), 2) AS cogs,
    ROUND(SUM(i.quantity * (i.unit_price * (1 - i.discount) - p.unit_cost)), 2) AS gross_profit,
    ROUND(
        SUM(i.quantity * (i.unit_price * (1 - i.discount) - p.unit_cost)) * 100.0
        / NULLIF(SUM(i.quantity * i.unit_price * (1 - i.discount)), 0),
        1
    ) AS margin_pct
FROM products p
JOIN order_items i ON p.product_id = i.product_id
JOIN orders o ON i.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY p.product_id, p.name, p.category
ORDER BY gross_profit DESC
LIMIT 15;

-- 5. Channel completion and return rates
SELECT
    channel,
    COUNT(*) AS total_orders,
    SUM(status = 'Completed') AS completed,
    SUM(status = 'Returned') AS returned,
    SUM(status = 'Cancelled') AS cancelled,
    ROUND(AVG(status = 'Completed') * 100, 1) AS completion_rate,
    ROUND(AVG(status = 'Returned') * 100, 1) AS return_rate
FROM orders
GROUP BY channel
ORDER BY total_orders DESC;
