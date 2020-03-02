select (case when grade <8 THEN NULL ELSE name END) as name, grade, marks
from
(select name, grade, marks
from students, grades
where marks between min_Mark and Max_Mark) as t
order by grade desc, name, marks ;
