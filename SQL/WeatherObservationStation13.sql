select round(sum(lat_n),4)
from STATION
where lat_n between 38.7880 and 137.2345
order by lat_n
