-- lists the number of records with the same score in the table.
SELECT score, COUNT(*) as numbre FROM second_table GROUP BY score ORDER BY numbre DESC;
