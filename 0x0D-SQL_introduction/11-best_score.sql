-- Lists all records in the table second_table score >= 10 in my MySQL server.
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10 ORDER BY `score` DESC;
