## Working with databases

> In computing, a database is an organized collection of data stored and accessed electronically from a computer system

### Key features

    * Domain (Data Driven design)
    * DB Engine (deeserveste aplicatii client)
    * Data Hierarchy/ Architecture
    * Interfacing technology (language)  - the most popular SQL
    * Enterprize ready 
    * Security
    * Licensing
    * Popularity

## PG
    * Data Hierarchy
    - Server
    - Database
    - Table
        -Record(row)
            -Field(col)
                -KEY, TYPE, CONSTRAINT

    * SQL (Syntax, Statements)
    * DDL (Typing), DML (CRUD)
    * relations
    * ACID
    * Transactions
    * Normal forms



products
----------------------------
id | name      | category_id

----------------------------
  1 | "iPhone"  |  1       |
----------------------------
  ? | "Samsung" |  1       |
----------------------------
  2 | "Galaxy"  |  1       |
----------------------------
  3 | "SmartX"  |  null    |
----------------------------


prices
-----------------------------
amount | currency| product_id 
-----------------------------
-----------------------------
  1000 |  "USD"   | 1       |
-----------------------------
  1100 |  "USD"   | 2       |
-----------------------------
  900  |  "USD"   | 3       |
-----------------------------
  100  |  "USD"   | 1       |
-----------------------------

 categories
----------------------
id | name   
----------------------
1  | "Smartphones"
----------------------
2  | "AI"
----------------------









DB(relational) Key Moments:
- KEYS:
    * primary (unique, distinct) (integer, uuid, sku, guid, isbn...)
    * foreign (reference: insert validation, CASCADING - update, delete2)
- IDENTITY
    * AUTO INCREMENT ( SERIAL / IDENTITY )
    OPTIMISTIC APPOROACH  
- NORMAL FORMS
- CONSTRAINTS
- DATA TYPES
- INDEX
- TRANSACTIONS











ORM = Object Relational Mapper

[App](python)<--- db logic ---> <-- driver/connector (psycopg) -->PG database

1. connect
2. query
3. result


