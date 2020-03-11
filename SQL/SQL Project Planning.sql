set sql_mode = '';
select start_date, end_date

from (

    /* If end date is present in start date, this implies the project is in progress */
select start_date 
from projects
where start_date not in ( select end_date from projects)
) A

join

(
    /* If start date is in end date, this implies  that the specific date is a consecutive date previously moved from end to start, hence project is going on */
    
select end_date 
from projects
where end_date not in ( select start_date from projects)
) B
/* The cartesian product is not required, use logical filter to remove unnecessary records */

where start_date < end_date
group by start_date
ORDER BY DATEDIFF(End_Date, Start_Date), Start_Date
