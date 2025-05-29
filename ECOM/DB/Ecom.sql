create database ecom;
use ecom;
CREATE TABLE Shops (
    shop_id INT AUTO_INCREMENT PRIMARY KEY,
    shop_name VARCHAR(100) NOT NULL
);

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    shop_id INT,
    FOREIGN KEY (shop_id) REFERENCES Shops(shop_id)
);
CREATE TABLE Stock (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT DEFAULT 0,
    shop_id INT,
    FOREIGN KEY (shop_id) REFERENCES Shops(shop_id)
);
CREATE TABLE OrderMaster (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    shop_id INT,
    customer_id INT,
    order_date DATE,
    order_time TIME,
    FOREIGN KEY (shop_id) REFERENCES Shops(shop_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE OrderDetail (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    item_id INT,
    quantity INT DEFAULT 1,
    FOREIGN KEY (order_id) REFERENCES OrderMaster(order_id),
    FOREIGN KEY (item_id) REFERENCES Stock(item_id)
);
select * from Shops;
select * from Customers;
select * from Stock ;
select * from OrderMaster;
select * from OrderDetail;