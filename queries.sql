CREATE DATABASE Codeyug

SHOW DATABASES

CREATE TABLE IF NOT EXISTS tutorial(
    Video_id INT PRIMARY KEY,
    Video_name VARCHAR(100) NOT NULL,
    Video_views INT,
    Watchtime FLOAT
)

DESC tutorial


INSERT INTO tutorial
(Video_id, Video_name, Video_views Watchtime) VALUES
(101, 'oop basics', 15000, 100);