import mysql.connector
from CityDAO import CityDAO
from Customer import Customer
from City import City

class CustomerDAO:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="mydatabase"
        )

    def read(self, id: int):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM customer WHERE id = %s", (id, ))

        raw_customer = mycursor.fetchone()

        cityDAO = CityDAO()
        a_city = cityDAO.read(raw_customer[2])

        customer = Customer(raw_customer[1], City(a_city.id, a_city.name), raw_customer[0])
            
        return customer

    def readAll(self) -> list:
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM customer")

        raw_customers = mycursor.fetchall()

        customers = []
        cityDAO = CityDAO()
        for a_customer in raw_customers:
            a_city = cityDAO.read(a_customer[2])
            customers.append(Customer(a_customer[0], a_customer[1], City(a_city.id, a_city.name)))
            
        return customers

    def create(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = "INSERT INTO customer (customer_name, city_id) VALUES (%s, %s)"
        val = (entity.name, entity.city.id)

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("Customer name must be between 2 and 255 characters long")

        return mycursor.lastrowid

    def update(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = "UPDATE customer SET customer_name = %s, city_id = %s WHERE id = %s"
        val = (entity.name, entity.city.id, entity.id)

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("Customer name must be between 2 and 255 characters long")

        return mycursor.rowcount

    def delete(self, id: int) -> bool:
        mycursor = self.connection.cursor()

        sql = "DELETE FROM customer WHERE id = %s"
        adr = (id, )
        
        try:
            mycursor.execute(sql, adr)
            self.connection.commit()
            
        except mysql.connector.errors.IntegrityError:
            print("Customer cannot be deleted because there is a customer using it!")

        return mycursor.rowcount
