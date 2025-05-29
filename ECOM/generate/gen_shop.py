from modules.shop import Shop

def generate_shops():
    shop = Shop()
    shop.insert_shops(100)  # Fixed at 100 shops

if __name__ == "__main__":
    generate_shops()
