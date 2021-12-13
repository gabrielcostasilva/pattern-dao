# Python Data Access - Unit Tests
This project implements the [DAO pattern](http://www.corej2eepatterns.com/DataAccessObject.htm) as a way to practice data access with Python. It uses the _MySQL Connector_ [MySQL driver](https://www.w3schools.com/python/python_mysql_getstarted.asp) for basic MySQL data access.

This branch solves an issue pointed out in the `main` branch: **the lack of unit tests**.

If you want to understand this project, please check the [`main` branch](https://github.com/gabrielcostasilva/python-data-access) first.

## The Problem
In the original code, each DAO class has a `main` method that 'tests' the code. A unit test uses _assertions_ in a set of controlled procedures to show that the tested code works as expected.

Unit tests are considered a good programming practice. Moreover, unit tests give you confidence for changing your code. If your tests fail after a change, you _know_ your change broke the code.

_Notice that the lack of tests in the original project is prompted due to my lack of Python skills. This project evolves as I learn Python tools, techniques and features._

## The Solution
The solution is creating unit tests by using a library or framework. The `unittest` module is a vanilla Python solution for unit testing. We followed [Socratica's tutorial](https://www.youtube.com/watch?v=1Lfv5tUGsn8) to implement unit tests in this project.

We created two test classes - one for each DAO. Test classes extend `unittest.TestCase`. Each method in these classes tests a feature.

We tested the five CRUD methods for expected results, i.e. that the `create()` creates, the `update()` updates, etc. In addition, we tested exceptions, like when you try to add an already existing city. 

## The Cost
Creating tests increases coding effort, but it pays off when your code evolves. I am a particular fan of [test-driven development](https://www.youtube.com/watch?v=DD1fEhcEzY8), but that is really hard to do when one has little knowledge in the technology. 

Notice that our tests do not sanitise the database after creating, updating, etc. Therefore, you must use a test database.

## Warning
Our unit tests are hitting the database. Therefore, this strategy requires a test database. One possible alternative is using [test containers](https://www.youtube.com/watch?v=v3eQCIWLYOw).

Another solution is using mocks, but they could hide issues in the DAO. 