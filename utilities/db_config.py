import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_testing():
    """Create and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(

            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),

        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

conn = get_db_testing()
