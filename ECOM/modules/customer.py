from config.db import DBConnection
from faker import Faker

class Customer:
    def __init__(self):
        self.conn, self.cursor = DBConnection().get_connection()
        self.fake = Faker()

    def insert(self, name, shop_id):
        self.cursor.execute("INSERT INTO Customers (customer_name, shop_id) VALUES (%s, %s)", (name, shop_id))
        self.conn.commit()

    def insert_customers(self, shops=100, per_shop=100):
        self.cursor.execute("SELECT COUNT(*) FROM Customers")
        existing = self.cursor.fetchone()[0]
        expected = shops * per_shop

        if existing >= expected:
            print("Customers already exist. Skipping insert.")
            return

        for shop_id in range(1, shops + 1):
            for _ in range(per_shop):
                name = self.fake.name()
                self.insert(name, shop_id)

        print(f"✅ Inserted {expected - existing} customers (Total: {expected})")
