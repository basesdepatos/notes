
@symn369 
## DML

@Sosoloogic 
## DDL


## DCL 

**DCL (Data Control Language)** is a subset of SQL used to control access to data in a database. The main DCL commands are:

1. **GRANT**: Gives a user permission to access or modify database objects.
 - Example in sql:
 GRANT SELECT, INSERT ON table_name TO user_name;
     

2. **REVOKE**: Removes permissions previously granted to a user.
  - Example in sql:
  REVOKE SELECT, INSERT ON table_name FROM user_name;
     

These are the standard SQL commands but some databases can extend them to enhance security and role management. Some examples are DENY, SHOW GRANTS, CREATE ROLE, SET ROLE, DROP ROLE... 

DCL commands help manage user rights and control who can access or modify the data.


@YuUs01 
## TCL 

TCL (Transaction Control Language) is a subset of SQL used to manage transactions in a database. It helps ensure that database operations are completed successfully and maintain data integrity. The main TCL commands are:

1. **COMMIT**: Saves all changes made during the current transaction.
2. **ROLLBACK**: Undoes changes made during the current transaction, reverting the database to its previous state.
3. **SAVEPOINT**: Sets a point within a transaction to which you can later roll back.
4. **SET TRANSACTION**: Defines properties for the transaction, such as isolation level.

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


@YuUs01 
## SQL injection

SQL Injection (SQLi) is a cyber attack where attackers manipulate SQL queries in an application's code to gain unauthorized access to a database. This can allow them to steal, modify, or delete data, bypass authentication, or perform malicious actions on the database.

**How it works**: If an application does not properly sanitize user input, an attacker can inject malicious SQL code, altering the original query. For example, entering `1' OR '1' = '1` in a login form could bypass authentication by making the SQL query always return true.

**Prevention**:
- Use **prepared statements** or **parameterized queries** to separate data from code.
- **Validate and sanitize** user inputs.
- Limit database privileges (use the **least privilege principle**).
- Implement **Web Application Firewalls** (WAFs) to detect attacks.
- Avoid exposing detailed **error messages** that could provide insights into the database structure.

SQL injection is a critical security risk, but it can be prevented by following proper coding practices.
