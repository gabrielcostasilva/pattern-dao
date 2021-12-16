import mysql.connector
from CityDAO import CityDAO
from Customer import Customer
from City import City
from dao.AbstractDAO import AbstractDAO


class CustomerDAO(AbstractDAO):

    def get_main_table_name(self):
        return "customer"

    def fetch_single_entity(self, cursor):
        raw_customer = cursor.fetchone()

        cityDAO = CityDAO()
        a_city = cityDAO.read(raw_customer[2])

        return Customer(raw_customer[1], City(a_city.id, a_city.name), raw_customer[0])

    def fetch_many_entities(self, cursor):
        raw_customers = cursor.fetchall()

        customers = []
        cityDAO = CityDAO()

        for a_customer in raw_customers:
            a_city = cityDAO.read(a_customer[2])
            customers.append(Customer(a_customer[0], a_customer[1], City(a_city.id, a_city.name)))

        return customers

    def get_sql_insert_string(self):
        return "INSERT INTO customer (customer_name, city_id) VALUES (%s, %s)"

    def get_entity_attrs_for_insert(self, entity):
        return (entity.name, entity.city.id)

    def get_sql_update_string(self):
        return "UPDATE customer SET customer_name = %s, city_id = %s WHERE id = %s"

    def get_entity_attrs_for_update(self, entity):
        return (entity.name, entity.city.id, entity.id)
