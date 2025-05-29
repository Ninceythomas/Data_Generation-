import mysql.connector
class DBConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="N!ncey@2004#",
            database="ecom"
        )
        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn, self.cursor
