-- Depeding on the number of entries in information_schema.tables, the select statement will run untill @number becomes 1, then it won't repeat
set @number = 21;
select repeat('* ', @number := @number - 1) from information_schema.tables;
