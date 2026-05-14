-- sample.sqlite3 에 연결 후 이 파일 전체를 실행하세요.

DROP TABLE IF EXISTS PurchaseItem;
DROP TABLE IF EXISTS Purchase;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS User;

CREATE TABLE User (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Product (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    StockQuantity INTEGER NOT NULL DEFAULT 0,
    CategoryId INTEGER NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Purchase (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL,
    TotalPrice REAL NOT NULL,
    Status TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE PurchaseItem (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    PurchaseId INTEGER NOT NULL,
    ProductId INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Price REAL NOT NULL
);

-- User 데이터
INSERT INTO User (Username, Email, Password) VALUES ('alice', 'alice@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('bob', 'bob@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('choi', 'choi@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('ivan', 'ivan@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('fiona', 'fiona@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('jung', 'jung@example.com', 'hashed');
INSERT INTO User (Username, Email, Password) VALUES ('kim', 'kim@example.com', 'hashed');

-- Product 데이터
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Running Shoes', 89.0, 10, 1);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Wool Sweater', 79.0, 5, 1);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Slim Jeans', 59.9, 0, 2);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Cargo Pants', 64.0, 3, 2);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Chelsea Boots', 139.0, 7, 5);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Puffer Jacket', 129.0, 0, 3);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Trench Coat', 119.0, 2, 3);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Denim Jacket', 69.9, 4, 3);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Canvas Sneakers', 59.0, 0, 1);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Cardigan', 55.0, 6, 4);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Chino Pants', 54.9, 0, 2);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Graphic Tee', 22.9, 15, 4);
INSERT INTO Product (Name, Price, StockQuantity, CategoryId) VALUES ('Sports Socks', 9.9, 20, 4);

-- Purchase 데이터
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (1, 228.0, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (1, 359.5, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (2, 89.0, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (2, 323.0, 'pending');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (3, 389.9, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (4, 119.0, 'pending');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (5, 194.0, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (6, 79.0, 'completed');
INSERT INTO Purchase (UserId, TotalPrice, Status) VALUES (7, 64.0, 'completed');

-- PurchaseItem 데이터
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (1, 1, 1, 89.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (1, 2, 1, 79.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (1, 10, 1, 55.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (2, 5, 1, 139.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (2, 7, 1, 119.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (2, 8, 1, 69.9);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (3, 1, 1, 89.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (5, 4, 1, 64.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (5, 7, 1, 119.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (5, 8, 1, 69.9);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (7, 5, 1, 139.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (7, 1, 1, 89.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (8, 2, 1, 79.0);
INSERT INTO PurchaseItem (PurchaseId, ProductId, Quantity, Price) VALUES (9, 4, 1, 64.0);
