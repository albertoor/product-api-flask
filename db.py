import mysql.connector
from config import Configuration

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
                host = Configuration.MYSQL_HOST,
                port = Configuration.MSYQL_PORT,
                user = Configuration.MYSQL_USER,
                password = Configuration.MYSQL_PASSWORD,
                database = Configuration.MYSQL_DB
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def query(self, query, params=None):
        self.cursor.execute(query, params or())
        return self.cursor
    
    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()