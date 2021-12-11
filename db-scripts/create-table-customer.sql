CREATE TABLE customer(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    customer_name VARCHAR(255) NOT NULL,
    city_id int NOT NULL,
    CONSTRAINT name_gt_2_char CHECK (CHAR_LENGTH(customer_name) > 2),
    CONSTRAINT city_relationship FOREIGN KEY (city_id) REFERENCES city(id)
) DEFAULT CHARSET UTF8 COMMENT '';