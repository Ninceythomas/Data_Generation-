from modules.shop import Shop
from modules.customer import Customer
from modules.stock import Stock
from config.db import DBConnection
import random
import datetime

class Ecom:
    def __init__(self):
        self.shop_module = Shop()
        self.customer_module = Customer()
        self.stock_module = Stock()

        # Get DB connection and cursor here once for all operations
        self.conn, self.cursor = DBConnection().get_connection()

    def setup_data(self):
        self.shop_module.insert_shops(100)
        self.customer_module.insert_customers(shops=100, per_shop=100)
        self.stock_module.insert_stock(shops=100, per_shop=100)

    def generate_orders(self, num_orders=100000):
        # Fetch customers and their shops
        self.cursor.execute("SELECT customer_id, shop_id FROM Customers")
        customers = self.cursor.fetchall()

        # Fetch stock items and their shops — note 'item_id' instead of 'stock_id'
        self.cursor.execute("SELECT item_id, shop_id FROM Stock")
        items = self.cursor.fetchall()

        # Organize stock items by shop for fast lookup
        stock_by_shop = {}
        for item_id, shop_id in items:
            stock_by_shop.setdefault(shop_id, []).append(item_id)

        for _ in range(num_orders):
            customer_id, shop_id = random.choice(customers)
            order_date = datetime.date.today()
            order_time = datetime.datetime.now().time()

            # Insert into OrderMaster and get the generated order_id
            self.cursor.execute(
                "INSERT INTO OrderMaster (shop_id, customer_id, order_date, order_time) VALUES (%s, %s, %s, %s)",
                (shop_id, customer_id, order_date, order_time)
            )
            order_id = self.cursor.lastrowid

            # Randomly select 1-3 items from that shop's stock
            items_to_order = random.sample(stock_by_shop.get(shop_id, []), k=random.randint(1, 3))
            for item_id in items_to_order:
                quantity = random.randint(1, 10)
                self.cursor.execute(
                    "INSERT INTO OrderDetail (order_id, item_id, quantity) VALUES (%s, %s, %s)",
                    (order_id, item_id, quantity)
                )

        self.conn.commit()
