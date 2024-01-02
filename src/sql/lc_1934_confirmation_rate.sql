with totals As (
Select s.user_id,
CONVERT(DECIMAL(10, 2),count(action)) as total 
FROM confirmations c
Right Join Signups s
On c.user_id = s.user_id
group by s.user_id
),

tot_confirmed As (
Select s.user_id, 
CONVERT(DECIMAL(10, 2),count(action)) as total
FROM confirmations c
Right Join Signups s
On c.user_id = s.user_id
where action = 'confirmed'
group by s.user_id
)

Select t.user_id,
COALESCE(ROUND(tc.total / t.total, 2), 0) AS confirmation_rate 
from totals t
Left join tot_confirmed tc
on t.user_id = tc.user_id