CREATE DATABASE DB;
CREATE TABLE items(
	id INT UNIQUE,
	price INT,
	what CHAR(1)
)

SELECT id, price FROM items WHERE id = "ID"
SELECT id, price FROM items WHERE id = 1 ORDER BY 3#
SELECT id, price FROM items WHERE id = "0 union select 1, 2, 3#"
SELECT id, price FROM items WHERE id = 0 UNION SELECT 1, 2, 3#