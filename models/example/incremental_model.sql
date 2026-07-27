{{ config(
    materialized='incremental',
    unique_key=['id', 'event_date']
) }}

{% if is_incremental() %}
with max_date as (
    select coalesce(max(event_date), '2020-01-01'::date) as max_event_date
    from {{ this }}
)
{% endif %}

select
    id,
    item_id,
    event_date
from {{ ref('seed_data') }}
{% if is_incremental() %}
cross join max_date
where event_date >= max_event_date
{% endif %}
