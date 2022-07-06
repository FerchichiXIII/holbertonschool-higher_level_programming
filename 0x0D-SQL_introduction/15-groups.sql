-- lists the number of records with the same score in the table.
SELECT COUNT(*) `count` FROM second_table GROUP BY score;