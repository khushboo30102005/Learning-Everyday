# Introduction to Databases

## What is a Database?
**A database is a collection of related tables that together provide both a logical and conceptual view of data.**

### Why?
- Databases store data in structured tables → **logical structure**
- The conceptual view explains **how data is organized, related, and accessed**, independent of physical storage.

# What is DBMS?
A **Database Management System (DBMS)** is software that helps users create, store, manage, and manipulate databases.

### Key Features of DBMS
- Data storage and retrieval
- Data security and privacy
- Backup and recovery
- Concurrency control

## What is RDBMS?
A **Relational Database Management System (RDBMS)** stores data in tables (rows and columns) and supports relations using keys.

### Key Features
- Table-based storage
- Supports PK & FK
- Uses SQL
- Ensures data integrity

## What is MySQL?
**MySQL** is an open‑source RDBMS widely used in web applications.

### Key Features
- Free & open-source
- Uses SQL
- Scalable & secure
- Works with PHP, Java, Python, Node.js

## What is SQL?
**SQL** (Structured Query Language) is used to manage and retrieve data from relational databases.

### Key Features
- Querying data
- Data definition & manipulation
- Easy to learn
- Supports joins & conditions

## How to Communicate with MySQL?
You can communicate with MySQL using various tools and languages.

### Methods
1. **MySQL CLI**
   ```sql
   mysql -u username -p
   ```
2. **MySQL Workbench**
3. **Programming Languages** (Python, PHP, Java, Node.js)
4. **Web Tools** (phpMyAdmin, Adminer)

### Process
1. Connect → 2. Send Query → 3. Process → 4. Response

## What is a Primary Key?
A **Primary Key (PK)** uniquely identifies each record.

### Example
```sql
CREATE TABLE Students (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT
);
```

## What is a Foreign Key?
A **Foreign Key (FK)** links two tables.

### Example
```sql
CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  StudentID INT,
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

## What is a Record?
A **Record** is a row in a table.

### Example
| StudentID | Name     | Age |
|-----------|----------|-----|
| 101       | Khushboo | 22  |

## What is a Field?
A **Field** is a column in a table.

### Example
- StudentID → Field  
- Name → Field  
- Age → Field  

## Basic SQL Commands

### CREATE DATABASE
```sql
CREATE DATABASE mydatabase;
```

### USE
```sql
USE mydatabase;
```

### CREATE TABLE
```sql
CREATE TABLE Students (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT
);
```

### INSERT
```sql
INSERT INTO Students (StudentID, Name, Age)
VALUES (101, 'Khushboo', 22);
```

### SELECT
```sql
SELECT * FROM Students;
```

### UPDATE
```sql
UPDATE Students
SET Age = 23
WHERE StudentID = 101;
```

### DELETE
```sql
DELETE FROM Students
WHERE StudentID = 101;
```

### DROP TABLE
```sql
DROP TABLE Students;
```

### ALTER TABLE
```sql
ALTER TABLE Students ADD Email VARCHAR(50);
```

### WHERE Clause
```sql
SELECT * FROM Students WHERE Age > 20;
```
