```sqlite
CREATE TABLE ORDERS (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_in  DATETIME NOT NULL,
    time_out DATETIME,
    cost REAL NOT NULL,
    pickup   INTEGER  NOT NULL
);
```

```sqlite
CREATE TABLE PRODUCTS (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);
```

```sqlite
CREATE TABLE STAFF (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    position TEXT NOT NULL,
    labor_contract INTEGER NOT NULL
);
```

```sqlite
CREATE TABLE ORDERS (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_in DATETIME NOT NULL,
    time_out DATETIME,
    cost REAL NOT NULL,
    pickup INTEGER NOT NULL,
    staff INTEGER NOT NULL,
    
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);
```

```sqlite
PRAGMA foreign_keys = ON;
```

```sqlite
CREATE TABLE PRODUCTS_ORDERS (
    product_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product INTEGER NOT NULL,
    in_order INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id),
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
);
```

