# Python Data Access - Immutable Dataclasses
This project implements the [DAO pattern](http://www.corej2eepatterns.com/DataAccessObject.htm) as a way to practice data access with Python. It uses the _MySQL Connector_ [MySQL driver](https://www.w3schools.com/python/python_mysql_getstarted.asp) for basic MySQL data access.

This branch solves an issue pointed out in the `main` branch: **Dataclasses are not immutable**.

If you want to understand this project, please check the [`main` branch](https://github.com/gabrielcostasilva/python-data-access) first.

## The Problem
Mutable DTOs, _entities_, or _dataclasses_ might be a problem because their properties may unexpectedly change. For instance, consider you retrieved a `City` from `CityDAO`. One may inadvertently change the City name during processing. As a result, the client will have inconsistent data. 

## The Solution
Immutable classes have been strongly advocated among experienced developers as a way to mitigate issues with inconsistent data. They are easy to implement and may save hours of troubleshooting.

## The Cost
The cost is zero in this present project, as all tests passed after the change.

## Warning
No warnings to disclose.