from modules.customer import Customer

def generate_customers():
    customer = Customer()
    customer.insert_customers(shops=100, per_shop=100)  # 100 customers per 100 shops

if __name__ == "__main__":
    generate_customers()
