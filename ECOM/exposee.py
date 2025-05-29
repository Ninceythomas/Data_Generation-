from  generate.analytics import (
    get_db_connection,
    get_average_customers_per_shop,
    get_average_stocks_per_shop,
    get_total_shops
)

if __name__ == "__main__":
    conn = get_db_connection()
    cursor = conn.cursor()

    avg_customers = get_average_customers_per_shop(cursor)
    avg_stocks = get_average_stocks_per_shop(cursor)
    total_shops = get_total_shops(cursor)

    print(f"Average customers per shop: {avg_customers}")
    print(f"Average stocks per shop: {avg_stocks}")
    print(f"Total number of shops: {total_shops}")

    cursor.close()
    conn.close()
