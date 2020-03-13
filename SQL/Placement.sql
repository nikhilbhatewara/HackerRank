
select studentname
from
(
/* Get names and salary of student */
select s.id as studentid,s.name as studentname,p.salary as studentsalary
from students s 
join packages p on s.id = p.id
) as A

JOIN 
(
  /* Get names and salary of friend */  
select f.id as fstudentid,f.friend_id as friendid,p.salary as firendsalary
from friends f 
join packages p on f.friend_id = p.id

) as B

on A.studentid = B.fstudentid
where A.studentsalary < B.firendsalary
order by firendsalary

;
