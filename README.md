# Python Data Access - Template Method
This project implements the [DAO pattern](http://www.corej2eepatterns.com/DataAccessObject.htm) as a way to practice data access with Python. It uses the _MySQL Connector_ [MySQL driver](https://www.w3schools.com/python/python_mysql_getstarted.asp) for basic MySQL data access.

This branch solves an issue pointed out in the `main` branch: **It repeats itself a lot!**.

If you want to understand this project, please check the [`main` branch](https://github.com/gabrielcostasilva/python-data-access) first.

## The Problem
In the original code, each DAO implements CRUD methods to manage data in a database. As a result, each DAO repeats code systematically. This is sufficient to create a lot of useless repetition.  

## The Solution
The [Template Design Pattern](https://refactoring.guru/design-patterns/template-method) decreases code repetition by setting a _template_ that is shared by all DAOs through inheritance.

The `AbstractDAO` class creates the traditional DAO structure (_template_) with CRUD methods. However, the class leaves the entity-specific parts of code open for change. This is done by overriding _abstract methods_.

For instance, reading data requires a SQL query string with the table name, like so:
```
mycursor.execute(f"SELECT * FROM {self.get_main_table_name()} WHERE id = %s", (id,))
```
In the example above, we replace the table name in the SQL query string with a call to `get_main_table_name()`, which is an abstract method. This method is implemented in each DAO subclass, completing the code. See an example in the `CityDAO` class:
```
def get_main_table_name(self):
    return "city"
```

## The Cost
Although the code is easier to change as the main code is centralised in one single place (the `AbstractDAO` class), it increases the number of LoC. 

## Warning
Our implementation does not eliminate code repetition completely. For instance, the process for retrieving entity data must be implemented in each DAO class. 
