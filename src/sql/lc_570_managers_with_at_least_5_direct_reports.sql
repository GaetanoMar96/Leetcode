Select name
from Employee
Where id in (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING count(*) >= 5
)