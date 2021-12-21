from Customer import Customer
from dao.AbstractDAO import AbstractDAO


class CustomerDAO(AbstractDAO):

    def get_main_table_name(self):
        return "customer"

    def get_entity(self):
        return Customer()

    def get_sql_insert_string(self):
        return "INSERT INTO customer (customer_name, city_id) VALUES (%s, %s)"

    def get_entity_attrs_for_insert(self, entity):
        return (entity.name, entity.city.id)

    def get_sql_update_string(self):
        return "UPDATE customer SET customer_name = %s, city_id = %s WHERE id = %s"

    def get_entity_attrs_for_update(self, entity):
        return (entity.name, entity.city.id, entity.id)
