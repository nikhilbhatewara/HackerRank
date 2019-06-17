SELECT CEIL(AVG(SALARY) -  AVG(REPLACE(SALARY, '0', '')))
FROM EMPLOYEES

# The ceil function returns the smallest integer possible however round returns the largest integer possible
