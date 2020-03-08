/*
Enter your query here.
*/

select h.hacker_id, h.name, count(c.challenge_id) as challenge_created
from hackers h join challenges c on h.hacker_id = c.hacker_id
group by h.hacker_id, h.name
having  count(c.challenge_id) >= 
/* maximum number of challenges created by anyone */
(
 select max(T1.cid)
    from 
    (
    select count(challenge_id) as cid
    from challenges 
    group by hacker_id
        ) as T1
)


or challenge_created in 
/* those student who created only 1 challenge and it's not shared by anyone else */
(
 select T2.cid
    from 
    (
    select count(challenge_id) as cid
    from challenges 
    group by hacker_id
        ) as T2
    group by T2.cid
    having count(T2.cid) = 1
)

order by count(c.challenge_id) DESC,c.hacker_id
