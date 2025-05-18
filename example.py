import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = mysql.connector.connect(
        user = os.getenv('MYSQL_USER'),
        password = os.getenv('MYSQL_PASSWORD'),
        host = os.getenv('MYSQL_HOST'),
        port = int(os.getenv('MYSQL_PORT')),
        database = os.getenv('DATABASE')
    )
    if conn.is_connected():
        print("Connected")
except Exception as e:
    print("unnable to connect:", e)

cur = conn.cursor()
# cur.execute("CREATE DATABASE Codeyug")
# cur.execute("SHOW DATABASES")
# for data in cur:
#     print(data[0])
# cur.execute("USE codeyug")
# cur.execute("""
#         CREATE TABLE IF NOT EXISTS tutorial1(
#         Video_id INT PRIMARY KEY,
#         Video_name VARCHAR(100) NOT NULL,
#         Video_views INT,
#         Watchtime FLOAT
#     )
# """)

# cur.execute("DESC tutorial")
# for data in cur:
#     print(data[0])

sql = """
INSERT INTO tutorial
(Video_id, Video_name, Video_views, Watchtime) VALUES
(104, 'python basics', 25000, 20.0),
(105, 'exception basics', 12000, 30.4);
"""
try:
    cur.execute(sql)
    conn.commit()
    print("Successfully data inserted")
    print(f"{cur.rowcount} rows inserted")
except Exception as e:
    conn.rollback()
    print("Something went wrong", e)
cur.close()
conn.close()