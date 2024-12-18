## Database Concepts

### Interface in Databases

An **interface** in the context of databases refers to the mechanisms or points of interaction that allow users or external systems to communicate and work with the database. It abstracts the internal complexity of the system and provides a simple way to interact with the data.

### Integrity in Databases

**Integrity** in databases is a fundamental concept that ensures the accuracy, consistency, and validity of the stored data. It means that data must adhere to certain rules and constraints that ensure the information is reliable and coherent. There are several types of integrity in databases:

- **Entity Integrity**: Ensures that each row in a table has a unique primary key. This guarantees that each record is unique and there are no duplicates.
- **Referential Integrity**: Ensures that relationships between tables remain consistent. This is enforced through foreign keys, which guarantee that a value in one table exists in another related table.
- **Domain Integrity**: Ensures that the data in a column belongs to a specific range of values or data type. For example, if a column stores ages, it should restrict input to only positive integers.
- **User-Defined or Business Integrity**: These are rules that impose custom constraints on the data, based on business requirements. These rules ensure that the data meets certain logical conditions beyond those defined by the database.

### Integration

**Integration** in databases refers to combining data or systems from multiple sources into ada unified system, enabling them to work together. This could involve combining data from different databases or integrating a database with other software systems (e.g., through APIs).

### Metadata

**Metadata** is data that describes other data. In databases, metadata provides information about the structure, organization, and attributes of the data stored in the database. For example, metadata can describe the types of data in each column of a table, constraints, and relationships between tables. It helps users and systems understand how to access, use, and manage the data efficiently.

### Transactions

A **transaction** is a sequence of database operations that are executed as a single logical unit. Transactions must follow the **ACID** properties:

- **Atomicity**: Ensures that all operations within a transaction are completed; otherwise, none are applied.
- **Consistency**: Ensures that a transaction leaves the database in a valid state.
- **Isolation**: Prevents concurrent transactions from interfering with each other.
- **Durability**: Guarantees that once a transaction is committed, it remains persistent.

### Concurrency

**Concurrency** refers to the ability of the database to handle multiple transactions simultaneously. Concurrency control mechanisms are used to:

- Prevent conflicts, such as deadlocks or race conditions.
- Maintain consistency and isolation of transactions.
- Ensure fair resource sharing.

### Migration

**Migration** involves transferring data, applications, or entire systems from one database to another. Types of migration include:

- **Database Migration**: Moving data between different databases or versions.
- **Cloud Migration**: Transferring databases to cloud-based systems.
- **Schema Migration**: Altering database schema while preserving data integrity.

### Connectivity

**Connectivity** refers to the ability of a database to establish and maintain a connection between a client application and the database server, enabling the exchange of data and commands. It is essential for applications to access and interact with a database, whether it's for retrieving, updating, or managing data. Good connectivity ensures that database interactions are efficient and reliable.

### Replication

**Replication** is the process of copying and maintaining database objects, such as tables or entire databases, across multiple locations or servers to ensure consistency and availability. There are two main types:

- **Master-Slave Replication**
- **Multi-Master Replication**

### Distribution

**Distribution** refers to the way data is spread across multiple servers or locations. This can involve distributing data horizontally (by partitioning rows across different databases or servers) or vertically (by splitting different columns across different servers).
