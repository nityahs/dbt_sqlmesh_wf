
        
            delete from "dev"."main"."incremental_model" as DBT_INCREMENTAL_TARGET
            using "incremental_model__dbt_tmp20260721151304903079"
            where (
                
                    "incremental_model__dbt_tmp20260721151304903079".id = DBT_INCREMENTAL_TARGET.id
                    and 
                
                    "incremental_model__dbt_tmp20260721151304903079".event_date = DBT_INCREMENTAL_TARGET.event_date
                    
                
                
            );
        
    

    insert into "dev"."main"."incremental_model" ("id", "item_id", "event_date")
    (
        select "id", "item_id", "event_date"
        from "incremental_model__dbt_tmp20260721151304903079"
    )
  