

SELECT
    id::INTEGER,
    item_id,
    event_date
FROM "dev"."main"."seed_data"


WHERE event_date >= (
    SELECT COALESCE(MAX(event_date), '2020-01-01')
    FROM "dev"."main"."incremental_model"
)
