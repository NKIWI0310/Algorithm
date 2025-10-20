
select
    s.name
from
    salesperson s
where
    s.sales_id not in ( select 
        o.sales_id
        from
            orders o
                Left join
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED'
    )