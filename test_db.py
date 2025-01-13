import sqlite3

# Подключение к базе данных (если файла базы данных нет, он будет создан)
conn = sqlite3.connect('my_database.db')

# Создание объекта курсора
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS STAFF (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    position TEXT NOT NULL,
    labor_contract INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCTS (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ORDERS (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_in DATETIME NOT NULL,
    time_out DATETIME,
    cost REAL NOT NULL,
    pickup INTEGER NOT NULL,
    staff INTEGER NOT NULL,
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCTS_ORDERS (
    product_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product INTEGER NOT NULL,
    in_order INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id),
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
);
""")

# Вставка данных в STAFF
cursor.executemany("""
INSERT INTO STAFF (full_name, position, labor_contract)
VALUES (?, ?, ?)
""", [
    ('John Doe', 'Manager', 12345),
    ('Jane Smith', 'Cashier', 67890)
])

# Вставка данных в PRODUCTS
cursor.executemany("""
INSERT INTO PRODUCTS (name, price)
VALUES (?, ?)
""", [
    ('Apple', 0.50),
    ('Banana', 0.30),
    ('Orange', 0.70)
])

# Вставка данных в ORDERS
cursor.executemany("""
INSERT INTO ORDERS (time_in, time_out, cost, pickup, staff)
VALUES (?, ?, ?, ?, ?)
""", [
    ('2025-01-11 10:00:00', '2025-01-11 11:00:00', 15.00, 0, 1),
    ('2025-01-11 12:30:00', None, 20.00, 1, 2)
])

# Вставка данных в PRODUCTS_ORDERS
cursor.executemany("""
INSERT INTO PRODUCTS_ORDERS (product, in_order, amount)
VALUES (?, ?, ?)
""", [
    (1, 1, 10),  # 10 яблок в заказе 1
    (2, 1, 5)    # 5 бананов в заказе 1
])

# Чтение данных из всех таблиц
def print_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"Data from {table_name}:")
    for row in rows:
        print(row)
    print()

# Вывод данных из таблиц
tables = ['STAFF', 'PRODUCTS', 'ORDERS', 'PRODUCTS_ORDERS']
for table in tables:
    print_table_data(table)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
