/* Write your T-SQL query statement below */

with cte as (
    select *, lag(event_date) over (partition by player_id order by event_date asc) as prev_date , min(event_date) over (partition by player_id order by event_date asc) as first_login
    from Activity
)

select round(count(player_id)*1.00 / (select count(distinct player_id) from Activity), 2) as fraction
from cte
where prev_date is not null and datediff(day,first_login, event_date) = 1