import sqlite3
import threading

from settingsConfig import g_settingsConfig


class DatabaseConnection:
    def __init__(self, database_path):
        self.__database_path = database_path
        self.__lock = threading.Lock()

    def __enter__(self):
        self.__dbConn = sqlite3.connect(self.__database_path)
        return self

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.__dbConn.close()
        except AttributeError:
            pass

    def execute(self, sql, data=None):
        with self.__lock:
            cursor = self.__dbConn.cursor()
            if data is not None:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)
            self.__dbConn.commit()

    def getData(self, sql, data=None, all=False):
        with self.__lock:
            cursor = self.__dbConn.cursor()
            if data is not None:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)
            if all:
                return cursor.fetchall()
            return cursor.fetchone()


class DatabaseConnectionFactory:
    def __init__(self, database_path):
        self.__database_path = database_path

    def create_connection(self):
        return DatabaseConnection(self.__database_path)


databaseSession = DatabaseConnectionFactory(g_settingsConfig.DatabaseSettings["fullPath"])
