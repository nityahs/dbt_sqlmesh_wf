
    
    

select
    item_id as unique_field,
    count(*) as n_records

from "dev"."main"."full_model"
where item_id is not null
group by item_id
having count(*) > 1


