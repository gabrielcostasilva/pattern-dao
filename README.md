# Python Data Access - Logging
This project implements the [DAO pattern](http://www.corej2eepatterns.com/DataAccessObject.htm) as a way to practice data access with Python. It uses the _MySQL Connector_ [MySQL driver](https://www.w3schools.com/python/python_mysql_getstarted.asp) for basic MySQL data access.

This branch solves an issue pointed out in the `main` branch: **It lacks logging;**.

If you want to understand this project, please check the [`main` branch](https://github.com/gabrielcostasilva/python-data-access) first.

## The Problem
Application monitoring has long been regarded as a central player in keeping track of system's health and infrastructure costs, specially in cloud platforms. Without logging, system's administrators are unable to understand what is going on with their systems. 

## The Solution
Although there are elaborated solutions for logging, all we need here is python own logging mechanism.

The `Logger` class configures a `logger` object and provides the `update(payload:str)` method for printing logs in the console. 

Then, in the `AbstractDAO` class, we add a call to `Logger.update(str)` before and after the behaviour execution of each CRUD method.

When running `CityDAO_test` we get:

```
INFO 2021-12-31 14:35:11,784 - Creating operation called for City(name='Maringá', id=1)
INFO 2021-12-31 14:35:11,797 - Creating operation for City(name='Maringá', id=1) successfully returned 23
INFO 2021-12-31 14:35:11,836 - Creating operation called for City(name='Londrina', id=1)
INFO 2021-12-31 14:35:11,849 - Creating operation for City(name='Londrina', id=1) successfully returned 24
INFO 2021-12-31 14:35:11,849 - Creating operation called for City(name='Londrina', id=1)
INFO 2021-12-31 14:35:11,866 - Creating operation for City(name='Londrina', id=1) unsuccessfully returned 'Entity already exists!'
INFO 2021-12-31 14:35:11,911 - Creating operation called for City(name=None, id=1)
INFO 2021-12-31 14:35:11,916 - Creating operation for City(name=None, id=1) unsuccessfully returned 'Entity already exists!'
INFO 2021-12-31 14:35:11,965 - Creating operation called for City(name='Uraí', id=1)
INFO 2021-12-31 14:35:11,979 - Creating operation for City(name='Uraí', id=1) successfully returned 26
INFO 2021-12-31 14:35:11,980 - Deleting operation called for id 26
INFO 2021-12-31 14:35:12,000 - Deleting operation for id 26 successfully returned 1
INFO 2021-12-31 14:35:12,038 - Creating operation called for City(name='Nova Aliança do Ivaí', id=1)
INFO 2021-12-31 14:35:12,053 - Creating operation for City(name='Nova Aliança do Ivaí', id=1) successfully returned 27
INFO 2021-12-31 14:35:12,093 - Creating operation called for Customer(name='John Doe', city=City(name='Nova Aliança do Ivaí', id=27), id=1)
INFO 2021-12-31 14:35:12,104 - Creating operation for Customer(name='John Doe', city=City(name='Nova Aliança do Ivaí', id=27), id=1) successfully returned 3
INFO 2021-12-31 14:35:12,106 - Deleting operation called for id 27
INFO 2021-12-31 14:35:12,112 - Deleting operation for id 27 unsuccessfully returned 'Entity cannot be deleted because there is a customer using it!'
INFO 2021-12-31 14:35:12,147 - Deleting operation called for id 0
INFO 2021-12-31 14:35:12,155 - Deleting operation for id 0 successfully returned 0
INFO 2021-12-31 14:35:12,200 - Creating operation called for City(name='Jussara', id=1)
INFO 2021-12-31 14:35:12,219 - Creating operation for City(name='Jussara', id=1) successfully returned 28
INFO 2021-12-31 14:35:12,220 - Reading all operation called
INFO 2021-12-31 14:35:12,228 - Reading all operation returned [City(name=28, id='Jussara'), City(name=24, id='Londrina'), City(name=23, id='Maringá'), City(name=27, id='Nova Aliança do Ivaí')]
INFO 2021-12-31 14:35:12,265 - Creating operation called for City(name='Jataizinho', id=1)
INFO 2021-12-31 14:35:12,277 - Creating operation for City(name='Jataizinho', id=1) successfully returned 29
INFO 2021-12-31 14:35:12,278 - Reading operation called for id '29'
INFO 2021-12-31 14:35:12,284 - Reading operation called for id '29' returned City(name='Jataizinho', id=29)
INFO 2021-12-31 14:35:12,324 - Creating operation called for City(name='Paraíso do Norte', id=1)
INFO 2021-12-31 14:35:12,351 - Creating operation for City(name='Paraíso do Norte', id=1) successfully returned 30
INFO 2021-12-31 14:35:12,352 - Updating operation called for City(name='Nova Esperança', id=30)
INFO 2021-12-31 14:35:12,376 - Updating operation for City(name='Nova Esperança', id=30) successfully returned 1
INFO 2021-12-31 14:35:12,414 - Creating operation called for City(name='Loanda', id=1)
INFO 2021-12-31 14:35:12,430 - Creating operation for City(name='Loanda', id=1) successfully returned 31
INFO 2021-12-31 14:35:12,430 - Creating operation called for City(name='Santa Fé', id=1)
INFO 2021-12-31 14:35:12,447 - Creating operation for City(name='Santa Fé', id=1) successfully returned 32
INFO 2021-12-31 14:35:12,448 - Updating operation called for City(name='Santa Fé', id=31)
INFO 2021-12-31 14:35:12,459 - Updating operation for City(name='Santa Fé', id=31) unsuccessfully returned 'Entity already exists!'
INFO 2021-12-31 14:35:12,503 - Creating operation called for City(name='Cornélio Procópio', id=1)
INFO 2021-12-31 14:35:12,516 - Creating operation for City(name='Cornélio Procópio', id=1) successfully returned 33
INFO 2021-12-31 14:35:12,517 - Updating operation called for City(name='', id=33)
```

## The Cost
As this project uses the _template method_ design pattern, the cost of introducing logging is low even if we have many DAOs . 

However, in  real project, I would consider using the _observer_ pattern to implementing logging. In addition, I would use the _chain of responsibility_ by creating a pre- and post-processor for each CRUD method. I believe these measure would considerably reduce coupling and enhance maintainability.


## Warning
By introducing logging, we removed console printing calls previously used in the exception handlers.

