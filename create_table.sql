CREATE TABLE customer_details (
    customer_id VARCHAR(50) NOT NULL,
    customer_unique_id VARCHAR(50) NOT NULL,
    customer_zip_code_prefix VARCHAR(10) NOT NULL,
    customer_city VARCHAR(50) NOT NULL,
    customer_state VARCHAR(10) NOT NULL,
    PRIMARY KEY (customer_id)
);

CREATE TABLE seller_details (
    seller_id VARCHAR(50) NOT NULL,
    seller_zip_code_prefix VARCHAR(10) NOT NULL,
    seller_city VARCHAR(50) NOT NULL,
    seller_state VARCHAR(10) NOT NULL,
    PRIMARY KEY (seller_id)
);

CREATE TABLE products_details ( 
    product_id VARCHAR(50) NOT NULL,
    seller_id VARCHAR(50) NOT NULL,
    product_category_name VARCHAR(50) NOT NULL,
    quantity_remaining INT NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (seller_id) REFERENCES seller_details (seller_id)
);

CREATE TABLE orders_details (
    order_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    seller_id VARCHAR(50) NOT NULL,
    order_status VARCHAR(50) NOT NULL,
    order_purchase_date DATE NOT NULL,
    order_delivered_carrier_date DATE NOT NULL,
    order_delivered_customer_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customer_details (customer_id),
    FOREIGN KEY (seller_id) REFERENCES seller_details (seller_id)
);

CREATE TABLE order_payments_details (
    order_id VARCHAR(50) NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    payment_installments INT NOT NULL,
    payment_value FLOAT NOT NULL,
    PRIMARY KEY (payment_sequential),
    FOREIGN KEY (order_id) REFERENCES orders_details (order_id)
);

CREATE TABLE order_items_details (
    order_id VARCHAR(50) NOT NULL,
    order_item_id VARCHAR(50) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    shipping_limit_date DATE NOT NULL,
    price FLOAT NOT NULL,
    freight_value FLOAT NOT NULL,
    PRIMARY KEY (order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders_details (order_id),
    FOREIGN KEY (product_id) REFERENCES products_details (product_id)
);