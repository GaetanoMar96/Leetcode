WITH LEAF AS (
    SELECT id
    FROM Tree
    where id NOT in (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL)
)

SELECT
    id,
    CASE WHEN p_id IS NULL THEN 'Root'
         WHEN id IN (SELECT * FROM LEAF) THEN 'Leaf'
         ELSE 'Inner' END AS type
FROM Tree