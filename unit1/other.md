
## DML

In databases, **DML** stands for **Data Manipulation Language**. It is a subset of SQL (Structured Query Language) used to manipulate data stored in a database. DML commands allow users to retrieve, insert, update, and delete data within database tables. These operations interact with the data stored in the database but do not change the database's structure.

### Key DML Commands:
- **SELECT**: Retrieves data from one or more tables.
   
   - `SELECT * FROM employees WHERE department = 'Sales'`;
   
- **INSERT**: Adds new records to a table.
   
   - `INSERT INTO employees (name, department, salary) VALUES ('John Doe', 'Sales', 50000)`;
   
- **UPDATE**: Modifies existing records in a table.
   
   - `UPDATE employees SET salary = 55000 WHERE name = 'John Doe'`;
   
- **DELETE**: Removes records from a table.
   
   - `DELETE FROM employees WHERE name = 'John Doe'`;
   

### Characteristics of DML:
- **Transactional**: DML operations can be rolled back or committed, depending on whether the operation succeeds or fails.
- **Non-structural**: These commands do not alter the schema or structure of the database, unlike DDL (Data Definition Language) commands such as `CREATE` or `ALTER`.
- **Data-Focused**: DML is all about interacting with the data, enabling CRUD (Create, Read, Update, Delete) operations.

### DML vs. Other SQL Subsets:
- **DDL (Data Definition Language)**: Manages database schema and structure.
- **DCL (Data Control Language)**: Controls access and permissions.
- **TCL (Transaction Control Language)**: Manages database transactions. 

DML is central to most database interactions, enabling dynamic data manipulation in a database system.

## DDL

**DDL (Data Definition Language)** is a type of SQL used to define and manage database structures, like tables, schemas, and indexes. It doesn't deal with the data itself but with the structure that holds the data. 

Here are the main DDL commands:

- **CREATE**: Used to create new database objects like tables, views, or schemas.
   - Example: **`CREATE TABLE students (id INT, name VARCHAR(50));`**  
     This creates a new table called "students" with two columns: "id" and "name".

- **ALTER**: Used to modify an existing database object (e.g., adding a new column to a table).
   - Example: **`ALTER TABLE students ADD age INT;`**  
     This adds a new "age" column to the "students" table.

- **DROP**: Used to delete a database object, like a table or a column.
   - Example: **`DROP TABLE students;`**  
     This deletes the "students" table and all its data.

- **TRUNCATE**: Used to remove all rows from a table but keeps the table structure intact.
   - Example: **`TRUNCATE TABLE students;`**  
     This deletes all the rows in the "students" table but doesn't remove the table itself.

- **RENAME**: Used to rename a database object (like a table or column).
   - Example: **`RENAME students TO alumni;`**  
     This renames the "students" table to "alumni".

DDL helps you define, modify, and delete the structure of your database, but not the data inside it.

## DCL 

**DCL (Data Control Language)** is a subset of SQL used to control access to data in a database. The main DCL commands are:

- **GRANT**: Gives a user permission to access or modify database objects.
 - Example in sql:
 `GRANT SELECT, INSERT ON table_name TO user_name`;
     

- **REVOKE**: Removes permissions previously granted to a user.
  - Example in sql:
  `REVOKE SELECT, INSERT ON table_name FROM user_name`;
     

These are the standard SQL commands but some databases can extend them to enhance security and role management. Some examples are DENY, SHOW GRANTS, CREATE ROLE, SET ROLE, DROP ROLE... 

DCL commands help manage user rights and control who can access or modify the data.

## TCL 

**TCL (Transaction Control Language)** is a subset of SQL used to manage transactions in a database. It helps ensure that database operations are completed successfully and maintain data integrity. The main TCL commands are:

- **COMMIT**: Saves all changes made during the current transaction.
- **ROLLBACK**: Undoes changes made during the current transaction, reverting the database to its previous state.
- **SAVEPOINT**: Sets a point within a transaction to which you can later roll back.
- **SET TRANSACTION**: Defines properties for the transaction, such as isolation level.

TCL ensures that database operations are processed reliably and that data remains consistent, even if there are errors or system failures.

 
## Codd's 12 rules

**Codd's 12 rules** define what makes a database "relational."

1. Information Rule: Data is stored in tables.
2. Guaranteed Access Rule: Every data item is uniquely accessible using a table, row, and column.
3. Null Values: Handle missing values systematically.
4. Dynamic Catalog: Metadata (data structure) is stored in tables.
5. Comprehensive Language: The database should support a query language (SQL).
6. View Updating: Views (virtual tables) should be updateable.
7. Set Operations: Use set-based operations, not row-by-row.
8. Physical Independence: Changes in storage do not affect the database.
9. Logical Independence: Changes in schema should not affect applications.
10. Integrity Independence: Integrity rules are stored in the database.
11. Distribution Independence: Database should function the same regardless of physical location.
12. Non-Subversion: Low-level access cannot bypass relational rules.

These rules ensure data consistency, flexibility, and ease of use in relational databases.


## SQL injection

**SQL Injection (SQLi)** is a cyber attack where attackers manipulate SQL queries in an application's code to gain unauthorized access to a database. This can allow them to steal, modify, or delete data, bypass authentication, or perform malicious actions on the database.

**How it works**: If an application does not properly sanitize user input, an attacker can inject malicious SQL code, altering the original query. For example, entering `1' OR '1' = '1` in a login form could bypass authentication by making the SQL query always return true.

**Prevention**:
- Use **prepared statements** or **parameterized queries** to separate data from code.
- **Validate and sanitize** user inputs.
- Limit database privileges (use the **least privilege principle**).
- Implement **Web Application Firewalls** (WAFs) to detect attacks.
- Avoid exposing detailed **error messages** that could provide insights into the database structure.

SQL injection is a critical security risk, but it can be prevented by following proper coding practices.
