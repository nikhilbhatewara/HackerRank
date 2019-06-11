select round(sum(lat_n),2), round(sum(long_w),2)
from STATION
order by lat_n, long_w
