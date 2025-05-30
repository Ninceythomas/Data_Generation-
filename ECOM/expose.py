from main.all import Ecom

if __name__ == "__main__":
    ecommerce = Ecom()
    ecommerce.setup_data()
    ecommerce.generate_orders(num_orders = 100000)
    print("Inserted 100 shops, 10,000 customers, and 10,000 stock items.")

    
