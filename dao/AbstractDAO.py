from abc import ABC, abstractmethod

import mysql.connector


class AbstractDAO(ABC):

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="mydatabase"
        )

    @abstractmethod
    def get_main_table_name(self):
        pass

    @abstractmethod
    def get_entity(self):
        pass

    @abstractmethod
    def get_sql_insert_string(self):
        pass

    @abstractmethod
    def get_entity_attrs_for_insert(self, entity):
        pass

    @abstractmethod
    def get_sql_update_string(self):
        pass

    @abstractmethod
    def get_entity_attrs_for_update(self, entity):
        pass

    def read(self, id: int):
        mycursor = self.connection.cursor()
        mycursor.execute(f"SELECT * FROM {self.get_main_table_name()} WHERE id = %s", (id,))
        return self.get_entity().value_of(mycursor)

    def readAll(self) -> list:
        mycursor = self.connection.cursor()
        mycursor.execute(f"SELECT * FROM {self.get_main_table_name()}")

        return self.get_entity().of(mycursor)

    def create(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = self.get_sql_insert_string()
        val = self.get_entity_attrs_for_insert(entity)

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.IntegrityError:
            print("Entity already exists!")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("Entity name must be between 2 and 255 characters long")

        return mycursor.lastrowid

    def update(self, entity) -> int:
        mycursor = self.connection.cursor()

        sql = self.get_sql_update_string()
        val = self.get_entity_attrs_for_update(entity)

        try:
            mycursor.execute(sql, val)
            self.connection.commit()

        except mysql.connector.errors.IntegrityError:
            print("Entity already exists!")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                print("Entity name must be between 2 and 255 characters long")

        return mycursor.rowcount

    def delete(self, id: int) -> bool:
        mycursor = self.connection.cursor()

        sql = f"DELETE FROM {self.get_main_table_name()} WHERE id = %s"
        adr = (id,)

        try:
            mycursor.execute(sql, adr)
            self.connection.commit()

        except mysql.connector.errors.IntegrityError:
            print("Entity cannot be deleted because there is a customer using it!")

        return mycursor.rowcount
