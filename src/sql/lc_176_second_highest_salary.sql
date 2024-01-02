WITH maxsalary AS (
    SELECT salary as SecondHighestSalary 
    from employee
    group by salary
    having salary < (select MAX(salary) from employee)
    order by salary desc
    limit 1
)

select 
    case when (select count(*) from employee ) <= 1
        then null
    else
        (select * from maxsalary) 
    end as SecondHighestSalary 
from employee
limit 1;