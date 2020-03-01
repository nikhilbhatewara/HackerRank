with africaCountriesCTE as (
select CO.NAME AS COUNTRYNAME, CI.NAME AS CITYNAME
from country CO
join city CI ON CO.CODE = CI.COUNTRYCODE
where continent = 'Africa' 
)
SELECT CITYNAME
FROM africaCountriesCTE;
