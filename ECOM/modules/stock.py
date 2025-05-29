from config.db import DBConnection
from faker import Faker
import random

class Stock:
    def __init__(self):
        self.conn, self.cursor = DBConnection().get_connection()
        self.fake = Faker()

    def insert(self, item_name, quantity, shop_id):
        self.cursor.execute("INSERT INTO Stock (item_name, quantity, shop_id) VALUES (%s, %s, %s)", (item_name, quantity, shop_id))
        self.conn.commit()

    def insert_stock(self, shops=100, per_shop=100):
        self.cursor.execute("SELECT COUNT(*) FROM Stock")
        existing = self.cursor.fetchone()[0]
        expected = shops * per_shop

        if existing >= expected:
            print("Stock already exists. Skipping insert.")
            return

        for shop_id in range(1, shops + 1):
            for _ in range(per_shop):
                item_name = self.fake.word().capitalize() + " Item"
                quantity = random.randint(10, 100)
                self.insert(item_name, quantity, shop_id)

        print(f"Inserted {expected - existing} stock items (Total: {expected})")
