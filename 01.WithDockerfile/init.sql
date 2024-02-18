-- init.sql

CREATE TABLE dev1.users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO dev1.users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO dev1.users (name, email) VALUES ('Bob', 'bob@example.com');