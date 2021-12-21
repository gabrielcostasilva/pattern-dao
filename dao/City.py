from dataclasses import dataclass

@dataclass
class City:
    name: str = ""
    id: int = 1

    @staticmethod
    def value_of(cursor):
        city_id, city_name = cursor.fetchone()
        return City(city_name, city_id)

    @staticmethod
    def of(cursor):
        result = [City(a_city[0], a_city[1]) for a_city in cursor.fetchall()]
        return result