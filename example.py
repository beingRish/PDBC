import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = mysql.connector.connect(
        user = os.getenv('MYSQL_USER'),
        password = os.getenv('MYSQL_PASSWORD'),
        host = os.getenv('MYSQL_HOST'),
        port = int(os.getenv('MYSQL_PORT'))
    )
    if conn.is_connected():
        print("Connected")
except Exception as e:
    print("unnable to connect:", e)

conn.close()