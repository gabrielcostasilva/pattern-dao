import unittest

from dao.City import City
from dao.CityDAO import CityDAO
from dao.Customer import Customer
from dao.CustomerDAO import CustomerDAO


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city_dao = CityDAO()
        cls.dao = CustomerDAO()

        a_city_id = cls.city_dao.create(City("Apucarana"))
        cls.a_city = City("Apucarana", a_city_id)

    def test_create_null_customer(self):
        self.assertEqual(self.dao.create(Customer(None, self.a_city)), 0)

    def test_create_customer(self):
        self.assertNotEqual(self.dao.create(Customer("Michael Jordan", self.a_city)), 0)

    def test_update_null_customer(self):
        customer_id = self.dao.create(Customer("Angelina Jolie", self.a_city))

        self.assertEqual(self.dao.update(Customer("", self.a_city, customer_id)), -1)

    def test_update_customer(self):
        customer_id = self.dao.create(Customer("Marrie Curry", self.a_city))

        self.assertEqual(self.dao.update(Customer("Marry Christmas", self.a_city, customer_id)), 1)

    def test_delete_inexisting_customer(self):
        self.assertEqual(self.dao.delete(0), 0)

    def test_delete_customer(self):
        customer_id = self.dao.create(Customer("Mc Donalds", self.a_city))
        self.assertEqual(self.dao.delete(customer_id), 1)

    def test_read_all_customer(self):
        self.dao.create(Customer("All Patinho", self.a_city))

        self.assertGreater(len(self.dao.readAll()), 0)

    def test_read_single_customer(self):
        customer_name = "All Gore"
        customer_id = self.dao.create(Customer(customer_name, self.a_city))

        self.assertEqual(self.dao.read(customer_id).name, customer_name)

