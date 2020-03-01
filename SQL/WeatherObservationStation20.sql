select 
 case when mod(count(lat_n),2) = 0 
 -- For even number of rows, median will be at the center
 then floor((count(lat_n)/2)-1)
-- For odd number of rows, median will be count/2 + 1
 else floor((count(lat_n)/2)-1+1)
 end as myoffset
into @myOffset
from station;

PREPARE STMT FROM 'select round(LAT_N,4) from station order by LAT_N limit 1 offset ?';
EXECUTE STMT USING @myOffset ;
