from City import City
from dao.AbstractDAO import AbstractDAO


class CityDAO(AbstractDAO):

    def get_main_table_name(self):
        return "city"

    def get_entity(self):
        return City()

    def get_sql_insert_string(self):
        return "INSERT INTO city (city_name) VALUES (%s)"

    def get_entity_attrs_for_insert(self, entity):
        return (entity.name, )

    def get_sql_update_string(self):
        return "UPDATE city SET city_name = %s WHERE id = %s"

    def get_entity_attrs_for_update(self, entity):
        return (entity.name, entity.id)
