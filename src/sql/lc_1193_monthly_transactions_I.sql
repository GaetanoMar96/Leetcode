
With approved AS (
  SELECT
  LEFT(trans_date, 7) as month,
  country,
  Count(*) as approved_count,
  Sum(amount) as approved_total_amount
  FROM Transactions 
  where state = 'approved'
  GROUP BY LEFT(trans_date, 7), country
), total AS (

SELECT
LEFT(trans_date, 7) as month,
country,
Count(*)  as trans_count,
Sum(amount) as trans_total_amount
FROM Transactions 
GROUP BY LEFT(trans_date, 7), country)


SELECT t.month, t.country,
trans_count, trans_total_amount,
COALESCE(approved_count, 0) approved_count,
COALESCE(approved_total_amount,0) approved_total_amount
FROM total t
LEFT JOIN approved a
ON a.month = t.month 
AND a.country = t.country