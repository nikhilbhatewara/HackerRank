
-- Create a common table expression
With totalscoreCTE AS 
(
-- compute total score and exclude scores which are less than or equal to 0    
 select hacker_id,sum(score) as totalscore
from (
-- compute the maximum score of each hacker id for each challenge
-- Hackerrank MySQL does not support CTE    
select hacker_id,challenge_id,max(score)as score
from submissions
group by hacker_id,challenge_id
    having max(score) > 0
) as T
group by hacker_id
    )
    
    select T.hacker_id,H.name,T.totalscore
    from totalscoreCTE T 
    join hackers H on T.hacker_id = H.hacker_id
    order by T.totalscore DESC, T.hacker_id ASC 
