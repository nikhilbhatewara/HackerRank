SELECT f1.X, f1.Y 
FROM Functions f1
INNER JOIN Functions f2 ON f1.X=f2.Y AND f1.Y=f2.X
GROUP BY f1.X, f1.Y
/* pairs having x=y should only be counted if there is another pair where x=y */
HAVING COUNT(f1.X)>1 
/* This is to avoid duplication */
or f1.X<f1.Y
ORDER BY f1.X 
