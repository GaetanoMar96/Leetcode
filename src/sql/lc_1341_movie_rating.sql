WITH bestuser AS (
  select name, count(u.user_id)
  from movierating mr
  inner join users u
  on u.user_id = mr.user_id
  group by name
  order by count(u.user_id) DESC, name
  limit 1),
bestmovie AS (
  select title, avg(rating)
  from movierating mr
  inner join movies m
  on m.movie_id = mr.movie_id
  where TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
  group by title
  order by avg(rating) DESC, title
  limit 1
)

select name as results
from bestuser 
union all
select title
from bestmovie