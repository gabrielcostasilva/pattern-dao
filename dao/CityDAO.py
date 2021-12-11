import mysql.connector
from City import City

class CityDAO:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="mydatabase"
        )

    def read(self, id: int):
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM city WHERE id = %s", (id, ))
        city_id, city_name = mycursor.fetchone()
        return City(city_id, city_name)

    def readAll(self) -> list:
        mycursor = self.connection.cursor()
        mycursor.execute("SELECT * FROM city")
        
        return [City(a_city[0], a_city[1]) for a_city in mycursor.fetchall()]

    def create(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = "INSERT INTO city (city_name) VALUES (%s)"
        val = (entity.name, )

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.IntegrityError:
            print("City already exists!")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("City name must be between 2 and 255 characters long")

        return mycursor.lastrowid

    def update(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = "UPDATE city SET city_name = %s WHERE id = %s"
        val = (entity.name, entity.id)

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.IntegrityError:
            print("City already exists!")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("City name must be between 2 and 255 characters long")

        return mycursor.rowcount

    def delete(self, id: int) -> bool:
        mycursor = self.connection.cursor()

        sql = "DELETE FROM city WHERE id = %s"
        adr = (id, )
        
        try:
            mycursor.execute(sql, adr)
            self.connection.commit()
            
        except mysql.connector.errors.IntegrityError:
            print("City cannot be deleted because there is a customer using it!")

        return mycursor.rowcount


def main():
    dao = CityDAO()
    # print(dao.readAll())
    # print(dao.create(City(1, "Londrina")))
    # print(dao.create({"city_name": "Londrina"}))
    # print(dao.update(City(1, "Maringá")))
    # print(dao.delete(2))
    # print(dao.read(1))


if __name__ == "__main__":
    main()
