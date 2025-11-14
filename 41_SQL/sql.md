# Basic SQL Commands --- Notes (Day 41)

## SHOW DATABASES

Purpose: Displays all databases present in the SQL server.

Example:

``` sql
SHOW DATABASES;
```

## CREATE TABLE

Purpose: Creates a new table within a selected database.

Example:

``` sql
CREATE TABLE Students (
  id INT,
  name VARCHAR(50),
  age INT
);
```

## INSERT INTO

Purpose: Inserts new records into a table.

Example:

``` sql
INSERT INTO Students (id, name, age)
VALUES (1, 'John Doe', 30);
```

## SELECT

Purpose: Retrieves data from a table.

Example:

``` sql
SELECT * FROM Students;
```

## DELETE

Purpose: Deletes existing records from a table.

Example:

``` sql
DELETE FROM Students WHERE id = 1;
```

------------------------------------------------------------------------

# Practical SQL Session Example

``` sql
CREATE DATABASE db1;
USE db1;

CREATE TABLE product (
  product_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(6,2),
  quantity INT
);

SHOW TABLES;
DESCRIBE product;

INSERT INTO product (name, price, quantity) VALUES
  ('coconut oil', 120.00, 5),
  ('colgate toothpaste', 150.00, 10),
  ('chips', 20.00, 50);

SELECT * FROM product;
SELECT name, price FROM product;
SELECT * FROM product WHERE quantity > 5;

UPDATE product SET price = 60 WHERE name = 'colgate toothpaste';

SELECT * FROM product;
```

``` text
Table View After Insert
---------------------------------------------
product_id | name               | price  | quantity
1          | coconut oil        | 120.00 | 5
2          | colgate toothpaste | 150.00 | 10
3          | chips              | 20.00  | 50

Table View After UPDATE
---------------------------------------------
product_id | name               | price  | quantity
1          | coconut oil        | 120.00 | 5
2          | colgate toothpaste | 60.00  | 10
3          | chips              | 20.00  | 50
```
