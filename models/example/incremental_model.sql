{{ config(
    materialized='incremental',
    unique_key=['id', 'event_date']
) }}

SELECT
    id,
    item_id,
    event_date
FROM {{ ref('seed_data') }}

{% if is_incremental() %}
where event_date >= (select coalesce(max(event_date), '2020-01-01') from seed_data)
{% endif %}
