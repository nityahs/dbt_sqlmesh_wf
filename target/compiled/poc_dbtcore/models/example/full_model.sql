

SELECT
    item_id,
    COUNT(DISTINCT id) AS num_orders
FROM "dev"."main"."incremental_model"
GROUP BY item_id