from abc import ABC, abstractmethod

import mysql.connector
from Logger import Logger


class AbstractDAO(ABC):

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="mydatabase"
        )

        self.logger = Logger()

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
        self.logger.update(f"Reading operation called for id '{id}'")

        mycursor = self.connection.cursor()
        mycursor.execute(f"SELECT * FROM {self.get_main_table_name()} WHERE id = %s", (id,))

        result = self.get_entity().value_of(mycursor)

        self.logger.update(f"Reading operation called for id '{id}' returned {result}")

        return result

    def readAll(self) -> list:
        self.logger.update(f"Reading all operation called")

        mycursor = self.connection.cursor()
        mycursor.execute(f"SELECT * FROM {self.get_main_table_name()}")

        result = self.get_entity().of(mycursor)

        self.logger.update(f"Reading all operation returned {result}")

        return result

    def create(self, entity) -> int:
        self.logger.update(f"Creating operation called for {entity}")

        mycursor = self.connection.cursor()

        sql = self.get_sql_insert_string()
        val = self.get_entity_attrs_for_insert(entity)
        result = 0

        try:
            mycursor.execute(sql, val)
            self.connection.commit()
            result = mycursor.lastrowid

            self.logger.update(f"Creating operation for {entity} successfully returned {result}")

        except mysql.connector.errors.IntegrityError as ie:
            self.logger.update(f"Creating operation for {entity} unsuccessfully returned 'Entity already exists!'")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                self.logger.update(f"Creating operation for {entity} unsuccessfully returned 'Entity name must be between 2 and 255 characters long'")

        return result

    def update(self, entity) -> int:
        self.logger.update(f"Updating operation called for {entity}")

        mycursor = self.connection.cursor()

        sql = self.get_sql_update_string()
        val = self.get_entity_attrs_for_update(entity)
        result = -1

        try:
            mycursor.execute(sql, val)
            self.connection.commit()
            result = mycursor.rowcount

            self.logger.update(f"Updating operation for {entity} successfully returned {result}")

        except mysql.connector.errors.IntegrityError:
            self.logger.update(f"Updating operation for {entity} unsuccessfully returned 'Entity already exists!'")

        except mysql.connector.errors.DatabaseError as error:
            if error.msg.startswith("Check constraint"):
                self.logger.update(
                    f"Updating operation for {entity} unsuccessfully returned 'Entity name must be between 2 and 255 characters long'")

        return result

    def delete(self, id: int) -> bool:
        self.logger.update(f"Deleting operation called for id {id}")

        mycursor = self.connection.cursor()

        sql = f"DELETE FROM {self.get_main_table_name()} WHERE id = %s"
        adr = (id,)
        result = -1

        try:
            mycursor.execute(sql, adr)
            self.connection.commit()
            result = mycursor.rowcount

            self.logger.update(f"Deleting operation for id {id} successfully returned {result}")

        except mysql.connector.errors.IntegrityError:
            self.logger.update(f"Deleting operation for id {id} unsuccessfully returned 'Entity cannot be deleted because there is a customer using it!'")

        return result
