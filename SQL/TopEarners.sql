select salary*months as earnings, count(*)
from employee
where salary*months = (select max(salary*months) from employee)
group by earnings
