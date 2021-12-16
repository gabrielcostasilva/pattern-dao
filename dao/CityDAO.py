from City import City
from dao.AbstractDAO import AbstractDAO


class CityDAO(AbstractDAO):

    def get_main_table_name(self):
        return "city"

    def fetch_single_entity(self, cursor):
        city_id, city_name = cursor.fetchone()
        return City(city_name, city_id)

    def fetch_many_entities(self, cursor):
        result = [City(a_city[0], a_city[1]) for a_city in cursor.fetchall()]
        return result

    def get_sql_insert_string(self):
        return "INSERT INTO city (city_name) VALUES (%s)"

    def get_entity_attrs_for_insert(self, entity):
        return (entity.name, )

    def get_sql_update_string(self):
        return "UPDATE city SET city_name = %s WHERE id = %s"

    def get_entity_attrs_for_update(self, entity):
        return (entity.name, entity.id)
