{{ config(
    materialized='incremental',
    unique_key=['id', 'event_date']
) }}

SELECT
    id::INTEGER,
    item_id,
    event_date
FROM {{ ref('seed_data') }}

{% if is_incremental() %}
WHERE event_date >= (
    SELECT COALESCE(MAX(event_date), '2020-01-01')
    FROM {{ this }}
)
{% endif %}
