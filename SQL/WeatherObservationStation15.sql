select round((long_w),4)
from STATION
where lat_n = ( select max(lat_n)
from STATION
where lat_n < 137.2345)
