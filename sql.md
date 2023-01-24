## 1) What is SQL?
SQL is a non-procedural programming language developed by IBM in the 1970s and then later by Oracle. SQL is used by almost all relational databases to write queries, access, edit, and retrieve data.

## 2) What is a database?
A database is an organized collection of digital information, or data, stored in a computer system. Unlike spreadsheets, a database can handle massive quantities of information while allowing multiple users access to the same database to run secure and independent queries.

## 3) What is an RDBMS, and how is it different from a traditional DBMS?
An RDBMS or Relational Database Management System is essentially a database utilizing a tabular schema to organize multiple data elements related to each other. An RDBMS lets your define, create, and maintain relational databases in addition to providing controlled access to the data within. A DBMS or Database Management System functions similarly to the RDBMS described above. However, DBMS data elements are stored as files rather than in tabular form, and there is no relationship between different data elements.

## 4) What is the difference between SQL and MySQL?
SQL is a programming language, while MySQL is a popular, open-source RDBMS. MySQL is used to store and organize data, while SQL is used to access, edit, update and maintain data in MySQL.

## 5) Explain the different types of SQL commands.
There are six basic types of SQL commands.
          Type	                          Description	                                Commands
Data Definition Language (DDL)	    Used to create and restructure       CREATE TABLE, ALTER TABLE, DROP TABLE
                                    relational database objects,        , CREATE INDEX, DROP VIEW
                                    such as tables.                      ALTER INDEX, DROP INDEX, CREATE VIEW

Data Manipulation Language (DML)	Used to manipulate data within
                                     relational database objects.	                  INSERT, UPDATE, DELETE

Data Query Language (DQL)	        With only one command, DQL is
                                    used to perform queries within
                                     a relational database.	                                    SELECT

Data Control Language (DCL)	        Used to control access to data 
                                    within a relational database.	   ALTER PASSWORD GRANT, REVOKE, CREATE SYNONYM

Data administration commands	    Used to analyze database                       START AUDIT, STOP AUDIT

                                    
Transactional control commands      operations or conduct audits  COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION     
	                                Used to manage transactions 
                                    within a relational database.	  

## 6) What is a PRIMARY KEY constraint?
A PRIMARY KEY constraint is a column (or combination of columns) used to designate each table row with a unique identifier. You can think of a primary key as having a similar function to national government-issued identification numbers, a citizen’s Social Security Number, or a vehicle identification number (VIN).

* Note: There’s a limit of one PRIMARY KEY constraint per table. All columns defined within a PRIMARY KEY constraint must be defined as NOT NULL.


## 7) What is a FOREIGN KEY constraint?
A FOREIGN KEY is a column or collection of fields in a table referencing a PRIMARY KEY in another table. The table containing the primary key is known as the parent table, and the table containing the foreign key is called the child table.

* For example, the PRIMARY KEY in the parent table below is OwnerID. The PRIMARY KEY uniquely identifies individual pet owners.

OwnerID	    LastName	    FirstName	    Address	        PetCount
2498	    Smith	        Bonnie	    123 Mango Street	2
2499	    Brown	        Thomas	    456 Papaya Way	    0
2450	    Goes	        Rosemary	789 Apple Court	    1

* For this child table, the PRIMARY KEY is PetID, and the OwnerID column is a FOREIGN KEY because it references the primary key of another table.

PetID	PetName	    Species	    OwnerID
1	    Whiskers	 Cat2          450
2	   Gilgamesh	Cockatiel	  2499
3	    Enkidu	    Cockatiel	  2499


## 8) What is a UNIQUE constraint?
Like the PRIMARY KEY, the UNIQUE constraint also ensures that each value is different from the others in its column. However, tables can have multiple columns with UNIQUE constraints, unlike the PRIMARY KEY constraint, limited to just one.

##  9) What are SQL joins? What are the different types of joins?
In SQL, a JOIN clause combines rows of data in different tables with a shared column. You can SELECT and return records with matching values in both tables based on this relationship.

There are four kinds of JOIN clauses in SQL:
        JOIN type	                                Description
INNER JOIN	                    Returns only the records with matching values in both tables.
LEFT JOIN	                    Returns records in the left table in addition to records with matching 
                                values in both tables.
RIGHT JOIN	                    Returns records in the right table, in addition to records with matching 
                                values in both tables.
FULL OUTER JOIN or FULL JOIN	Returns all records with matches in either the left or right tables.

## 10) What is a self join?
A JOIN clause combines rows from two or more tables based on a related column between them. A self join is a regular join, but the table is joined with itself – this is extremely useful for comparisons within a table.

Joining a table with itself means that each table row is combined with itself and with every other row of the table.

## 11) What is a cross join (Cartesian join)?
In SQL, the cross join combines each row of the first table with each row of the second table. It is also known as the Cartesian join since it returns the Cartesian product of the sets of rows from the joined tables.

## 12) What’s the difference between a WHERE clause and a HAVING clause?
The WHERE clause can be used to establish the first condition that groups and returns only the rows that meet that condition into a result set. Then, secondary conditions can be applied using the HAVING clause to return only the groups within that set that meet your new criteria.

## 13) What’s the difference between a TRUNCATE command and a DELETE command?
    Differences	                DELETE	                                          TRUNCATE

Type	                        DML (Data Manipulation Language)	        DDL (Data Definition Language)

Function	                     Used to remove specific rows 	            Used to delete all rows or 
                                or tuples from tables or relations.          tuples from a table.

WHERE	                        Can contain WHERE clause.	                Cannot contain WHERE clause.

Transaction                     logging	Row deletions are logged.	       Deleted data pages are not logged.

* The TRUNCATE command is faster than DELETE, but unlike the DELETE command, data cannot be rolled back after using it to recover data that has been mistakenly deleted.

## 14. What is a query?
In the context of this article, a query is a set of instructions written in a query language like SQL that allows an individual to access information held in a database.

15. What is a subquery?
A subquery or nested query is a query within a query.

There are two types of subqueries: Correlated and Non-correlated.

* Correlated subqueries refer to a column in a table specified by the FROM keyword of the main query.
* Non-correlated subqueries are independent and their output is substituted in the main query.

## 16) What are UNION, UNION ALL, MINUS, and INTERSECT set operators?
* The UNION operation combines the results of two or more SELECT statements. For example, getting the UNION of sets A and B, this operation would return all rows from both sets, excluding any duplicate rows.
* The UNION ALL operation does the same thing as UNION, but includes duplicate rows in its result set.
* The INTERSECT operation combines the results of two SELECT statements but only returns the rows with matching values in both sets.
* The MINUS operation combines the results of two SELECT statements but only returns rows with values that belong to the first set of the result.

## 17) What are Normalization and Denormalization?
Normalization refers to the methods used to remove redundancies and inconsistencies in a database.

* Denormalization refers to methods used to improve the performance of queries.
* Normalization introduces more tables to a database, whereas Denormalization reduces the number of tables.

## 18) What are scalar functions?
Scalar functions are defined by the user and return a single value (i.e., int, char, float, etc.) based on the input value.

Common SQL scalar functions:

* CONCAT() concatenates two or more character strings.
* FORMAT() sets the format to display a collection of values.
* LEN() calculates the total length of a given column.
* MID() extracts substrings from a collection of string values.
* ROUND() rounds the integer value for a numeric field.
* NOW() returns the current date and time.
* RAND() calculates a random collection of numbers of a given length.

## 19) What are aggregate functions?
In SQL, aggregate functions (also known as group functions) are applied to a group of values (or all values) to calculate and return a single value.

Common SQL aggregate functions:

* AVG calculates the average or mean of all values in a group.
* COUNT calculates the number of rows in group, including rows with NULL values.
* MIN and MAX returns the smallest and largest value in a group, respectively.
* SUM returns the sum of all non-NULL values in a group.
* STDDEV calculates the standard deviation.
* VARIANCE calculates the variance.

## 20) What is a stored procedure?
Instead of writing the same SQL query multiple times, you can save it as a stored procedure and call on it whenever necessary to execute it.
Store an SQL query:
```sql
CREATE PROCEDURE procedure_name
AS
sql_statements
GO;
```
Execute a stored procedure:
```sql
EXEC procedure_name;
```

## 21) What is the SELECT statement?
The SELECT statement is used in SQL queries to store specific data elements or fields from a table and return them in a result set.

The SELECTsyntax:
```sql
SELECT column_1, column_2, ...
FROM table_name;
```
To select all data elements from a table, use
```sql
SELECT * FROM table_name;
```

## 22) What is an index?
An SQL index is a lookup table used by the database search engine to find and retrieve data quickly. An index can help makeSELECT and WHERE clauses faster but can slow down the use of UPDATE and INSERT statements. ]

To create an index:
```sql
CREATE INDEX index_name ON table_name;
```
## 23) What are some common clauses used with SELECT queries in SQL?
The basic SQL SELECT statement contains three clauses:

* SELECT specifies the table columns to retrieve
* FROM specifies the tables to access
* WHERE is optional and specifies which rows in the FROM tables to use

The GROUP BY clause is used with aggregate functions to group the result set according to specified columns.

The HAVING clause functions similarly to the WHERE clause but allows the use of aggregate functions.

The ORDER BY clause sorts the result set in ascending (ASC) or descending (DESC) order according to a specified column.

When writing your SELECT queries, make sure that your syntax follows this order:
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

## 24) What are character manipulation functions?
Character manipulation functions can edit, change, or reformat character strings.

For example, you can concatenate two character strings by passing them into the CONCAT function using a SELECT query.

## 25) What is an SQL Server cursor? How do you use it?
When you want to process result sets one row at a time, you can use a database cursor, a control structure that allows you to traverse records in a database. Cursors can be used to point to individual rows in a group of rows.

You can DECLARE a cursor after any variable declaration.
```sql
DECLARE variable_name CHAR(20) 
DECLARE cursor_name CURSOR FOR
SELECT column_name 
FROM table_name
```

## 26) What are the different types of indexes?
* Clustered indexes are clustered together with the main body of data. A clustered index sorts and stores rows of data in a table or view sequentially, based on key values of the table to match the order of the index. There can only be one clustered index per table.
* Non-clustered indexes are separate from, and cannot be used to store or sort data in the main table. The key values of the index, and not the table are used to define the order of a non-clustered index.
* Column store indexes are a standard form of index that efficiently stores data in a column-based format, rather than row-oriented.
* Filtered indexes are used to index a section of rows within a table.
* Hash indexes are arrays, and use the Hash function F(K, N), where K is critical and N is the number of slots containing a pointer and row.
* Unique indexes assign unique values to every row of data, so that the index key does not contain any duplicates.

## 27) What is the difference between a clustered index and a non-clustered index?
The order of rows in a clustered index corresponds to the order of rows in the database. A table can only have one clustered index at a time.

A non-clustered index functions similarly to a clustered index, but is slower and creates a separate entity within the table that references the original table. A table can have multiple non-clustered indices.

## 28) What are ACID properties?
The ACID properties refer to properties that must be followed for transactions in a database management system to remain consistent.

* Atomicity: The entire transaction takes place at once or not at all.
* Consistency: A database must be consistent before and after a transaction takes place.
* Isolation: Transactions occur independently and can run concurrently with others.
* Durability: Updates to the database must be stored in and written to disk so that transaction records can     persist in the event of a system failure.

## 29) What is a schema?
An SQL schema is an abstract representation of logically structured data elements. Database schemas in SQL are defined at the logical level by a database user known as the schema owner.

## 30) What is an alias command?
The alias (AS) command makes columns or tables easier to read by giving them temporary names for the duration of a query.

## 31) How do you create empty tables with the same structure as another table?
You can use shallow cloning to create a copy of an existing table’s data structure and column attributes.
```sql
CREATE TABLE new_table LIKE table_1;
```
This command creates an empty table based on the parent table.

## 32) How do you select unique records from a table?
The SELECT DISTINCT clause will only return unique values from a table.

## 33) What is the default ordering of data using the order by clause? How could it be changed?
The default ordering of data is ascending (ASC). You can change the order by using the descending (DESC) keyword with the ORDER BY clause like so:
```sql
SELECT * FROM table_name ORDER BY column_name DESC;
```

## 34) What are some case manipulation functions in SQL?
* LOWER or LCASE takes in a given character string and converts it to lower case.
* UPPER or UCASE takes in a given character string and converts it to upper case.

## 35) What’s the standard syntax for group functions?
The general syntax is:
```sql
SELECT column_name, group_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name
ORDER BY column_name
```

## 36) What is the difference between CHAR and VARCHAR datatypes in SQL?
The character or CHAR datatype stores fixed length character strings. The variable character or VARCHAR datatype stores variable length character strings.

CHAR has better performance than VARCHAR, but VARCHAR can be useful for anticipating data values without a set length.

## 37) What are user-defined functions in SQL? What are the various types?
There are two types of functions in SQL:

* System Defined Functions (SDF) and
* User-Defined Functions (UDF)
User-Defined Functions (UDFs) are similar to functions found in programming languages. UDFs accept parameters, perform complex calculations, and return their results.

There are three types of UDFs:

* Scalar Functions return only a single value (scalar value) of any data type except text, ntext, image, cursor, and timestamp.
* Inline Table-Valued Functions return a table of values. Only one SELECT statement can be prepared by the return statement, and this statement defines the structure of the table that function returns.
* Multi-Statement Table-Valued Functions also return a table of values, but can contain multiple statements, and its table structure is defined by the user.
  
## 38) What is the difference between SQL and PL/SQL?
SQL is non-procedural and interacts directly with the database server. It’s easy to learn and use, but if you need to solve more complicated SQL problems and are willing to learn some more complex concepts, then PL/SQL can be a powerful tool.

PL/SQL is a procedural language that doesn’t interact directly with the database server but offers a faster processing speed and an expanded range of supported features. You can accomplish everything you need to do in SQL and more using PL/SQL.

PL/SQL:

* Can be used to write functions, packages, procedures, program blocks, and more.
* Supports for variables, conditional statements, and iterators.
* Supports error and exception handling.

## 39) What are entities and relationships?
An entity can be a real-world object that can be identified by a collection of related attributes or properties. An example of an entity in a zoo database might include zookeepers, veterinarians, different public outreach initiatives, or species of animals.

Relationships are connections between entities that are associated with each other.

The logical relationship between entities creates a database.

## 40) What is collation? What are the different collation sensitivity?
Collation is a configuration setting that specifies how a database sorts and compares data. Different collation rules can be configured to determine the correct character sequence used to sort the character data.

Collation sensitivity can be used to specify how different characters are treated.

* Accent sensitivity differentiates between a and á.
* Case sensitivity differentiates between A and a.
* Kana sensitivity differentiates between Japanese Hiragana and Katakana.
* Width sensitivity treats characters of different widths (single-byte and double-byte) differently.

