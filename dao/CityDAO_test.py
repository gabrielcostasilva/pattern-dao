import unittest

from dao.City import City
from dao.CityDAO import CityDAO
from dao.Customer import Customer
from dao.CustomerDAO import CustomerDAO


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = CityDAO()

    def test_create_null_city(self):
        self.assertEqual(self.dao.create(City(None)), 0)

    def test_create_existing_city(self):
        self.dao.create(City("Londrina"))
        self.assertEqual(self.dao.create(City("Londrina")), 0)

    def test_create_city(self):
        self.assertNotEqual(self.dao.create(City("Maringá")), 0)

    def test_update_null_city(self):
        city_id = self.dao.create(City("Cornélio Procópio"))

        self.assertEqual(self.dao.update(City("", city_id)), -1)

    def test_update_existing_city(self):
        city_id = self.dao.create(City("Loanda"))
        self.dao.create(City("Santa Fé"))

        self.assertEqual(self.dao.update(City("Santa Fé", city_id)), -1)

    def test_update_city(self):
        city_id = self.dao.create(City("Paraíso do Norte"))

        self.assertEqual(self.dao.update(City("Nova Esperança", city_id)), 1)

    def test_delete_inexisting_city(self):
        self.assertEqual(self.dao.delete(0), 0)

    def test_delete_city_in_relationship(self):
        city_name = "Nova Aliança do Ivaí"
        city_id = self.dao.create(City(city_name))

        CustomerDAO().create(Customer("John Doe", City(city_name, city_id)))

        self.assertEqual(self.dao.delete(city_id), -1)

    def test_delete_city(self):
        city_id = self.dao.create(City("Uraí"))
        self.assertEqual(self.dao.delete(city_id), 1)

    def test_read_all_cities(self):
        self.dao.create(City("Jussara"))

        self.assertGreater(len(self.dao.readAll()), 0)

    def test_read_single_city(self):
        city_name = "Jataizinho"
        city_id = self.dao.create(City(city_name))

        self.assertEqual(self.dao.read(city_id).name, city_name)
