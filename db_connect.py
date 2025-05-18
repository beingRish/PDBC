import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        db_connection = mysql.connector.connect(
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            host=os.getenv('MYSQL_HOST'),
            port=int(os.getenv('MYSQL_PORT')),
            database=os.getenv('DATABASE')
        )
        if db_connection.is_connected():
            print("Connected to database")
            return db_connection
    except Exception as e:
        print("Unable to connect:", e)
        return None
