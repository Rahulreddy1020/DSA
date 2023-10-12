



WITH FirstOrders AS (
    -- Identify the first order of each customer
    SELECT customer_id, MIN(order_date) as first_order_date
    FROM Delivery
    GROUP BY customer_id
)

, ImmediateFirstOrders AS (
    -- Find immediate first orders
    SELECT d.customer_id
    FROM Delivery d
    JOIN FirstOrders fo
    ON d.customer_id = fo.customer_id
    AND d.order_date = fo.first_order_date
    WHERE d.order_date = d.customer_pref_delivery_date
)

-- Calculate the percentage of immediate orders in the first orders of all customers
SELECT ROUND(100.0 * COUNT(ifo.customer_id) / COUNT(fo.customer_id), 2) as immediate_percentage
FROM FirstOrders fo
LEFT JOIN ImmediateFirstOrders ifo
ON fo.customer_id = ifo.customer_id;
