-- Lists all records in the table second_table with a score >= 10 in descwnding  my MySQL server.
SELECT `score`, `name` FROM `second_table`
WHERE `score` >= 10ORDER BY `score` DESC;
