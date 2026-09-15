-- Retail Business Intelligence
-- Reusable SQL analysis examples for the portfolio dataset.

-- 1. Revenue by category and year
SELECT
    category,
    year,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY category, year
ORDER BY year, total_revenue DESC;

-- 2. Category year-over-year comparison
WITH yearly AS (
    SELECT
        category,
        year,
        SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY category, year
)
SELECT
    category,
    year,
    total_revenue,
    LAG(total_revenue) OVER (
        PARTITION BY category ORDER BY year
    ) AS previous_year_revenue
FROM yearly
ORDER BY category, year;

-- 3. Top customers by lifetime spend
SELECT
    customer_id,
    customer_name,
    COUNT(*) AS total_orders,
    SUM(revenue) AS total_spend,
    AVG(revenue) AS avg_order_value
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_spend DESC
LIMIT 20;

-- 4. Product profitability
SELECT
    product_id,
    product_name,
    category,
    SUM(revenue) AS revenue,
    SUM(cogs) AS cogs,
    SUM(revenue - cogs) AS gross_profit,
    ROUND(
        100.0 * SUM(revenue - cogs) / NULLIF(SUM(revenue), 0),
        2
    ) AS margin_pct
FROM sales
GROUP BY product_id, product_name, category
ORDER BY gross_profit DESC;
