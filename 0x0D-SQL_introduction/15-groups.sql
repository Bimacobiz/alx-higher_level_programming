-- It will list the number of records that have the same score in the table second_table in my MySQL server.
-- The records will be placed in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
