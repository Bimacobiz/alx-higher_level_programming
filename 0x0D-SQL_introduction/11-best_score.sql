-- Will list all the records in the table second_table with a score >= 10 in my MySQL server.
-- It will order the records by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
