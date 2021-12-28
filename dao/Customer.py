from dataclasses import dataclass
from City import City
from CityDAO import CityDAO

@dataclass(frozen=True)
class Customer:
    name: str = ""
    city: City = City("")
    id: int = 1

    @staticmethod
    def value_of(cursor):
        raw_customer = cursor.fetchone()

        cityDAO = CityDAO()
        a_city = cityDAO.read(raw_customer[2])

        return Customer(raw_customer[1], City(a_city.id, a_city.name), raw_customer[0])

    @staticmethod
    def of(cursor):
        raw_customers = cursor.fetchall()

        customers = []
        cityDAO = CityDAO()

        for a_customer in raw_customers:
            a_city = cityDAO.read(a_customer[2])
            customers.append(Customer(a_customer[0], a_customer[1], City(a_city.id, a_city.name)))

        return customers