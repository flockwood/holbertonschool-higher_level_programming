-- Script that lists all records of the table second_table
-- Don't list rows where the name column does not contain a value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;