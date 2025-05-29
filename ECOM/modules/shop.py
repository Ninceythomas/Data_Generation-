from config.db import DBConnection
from faker import Faker

class Shop:
    def __init__(self):
        self.conn, self.cursor = DBConnection().get_connection()
        self.fake = Faker()

    def insert(self, name):
        self.cursor.execute("INSERT INTO Shops (shop_name) VALUES (%s)", (name,))
        self.conn.commit()

    def insert_shops(self, total=100):
        self.cursor.execute("SELECT COUNT(*) FROM Shops")
        existing = self.cursor.fetchone()[0]

        if existing >= total:
            print("100 shops already exist. Skipping insert.")
            return

        for _ in range(total - existing):
            name = self.fake.company()
            self.insert(name)

        print(f"Inserted {total - existing} shops (Total: {total})")
