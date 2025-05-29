import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # update if needed
        password="N!ncey@2004#",         # update if needed
        database="ecom"
    )

def get_average_customers_per_shop(cursor):
    cursor.execute("""
        SELECT AVG(customer_count) FROM (
            SELECT COUNT(*) AS customer_count
            FROM Customers
            GROUP BY shop_id
        ) AS sub;
    """)
    return cursor.fetchone()[0]

def get_average_stocks_per_shop(cursor):
    cursor.execute("""
        SELECT AVG(stock_count) FROM (
            SELECT COUNT(*) AS stock_count
            FROM Stock
            GROUP BY shop_id
        ) AS sub;
    """)
    return cursor.fetchone()[0]

def get_total_shops(cursor):
    cursor.execute("SELECT COUNT(*) FROM Shops")
    return cursor.fetchone()[0]
