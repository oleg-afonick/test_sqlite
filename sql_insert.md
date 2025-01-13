```sqlite
INSERT INTO STAFF (full_name, position, labor_contract) 
VALUES 
('John Doe', 'Manager', 12345),
('Jane Smith', 'Cashier', 67890);
```

```sqlite
INSERT INTO PRODUCTS (name, price) 
VALUES 
('Apple', 0.50),
('Banana', 0.30),
('Orange', 0.70);
```

```sqlite
INSERT INTO ORDERS (time_in, time_out, cost, pickup, staff) 
VALUES 
('2025-01-11 10:00:00', '2025-01-11 11:00:00', 15.00, 0, 1),
('2025-01-11 12:30:00', NULL, 20.00, 1, 2);
```

```sqlite
INSERT INTO PRODUCTS_ORDERS (product, in_order, amount) 
VALUES 
(1, 1, 10),  -- 10 яблок в заказе 1
(2, 1, 5);   -- 5 бананов в заказе 1
```