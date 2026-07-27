{{ config(
    materialized='table'
) }}

SELECT
    item_id,
    COUNT(DISTINCT id) AS num_orders
FROM {{ ref('incremental_model') }}
GROUP BY item_id
