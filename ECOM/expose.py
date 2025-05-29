from main.all import Ecom

if __name__ == "__main__":
    ecommerce = Ecom()
    ecommerce.setup_data()
    print("Inserted 100 shops, 10,000 customers, and 10,000 stock items.")
    ecommerce.evaluate_averages()
    