/*
Enter your query here.
*/

/*
Enter your query here.
*/

/*
Enter your query here.
*/

/*
Enter your query here.
*/

SELECT DISTINCT CITY
FROM STATION 
WHERE SUBSTRING(CITY, 1 ,1) NOT IN ('a','e','i','o','u','A','E','I','O','U') 
