import mysql.connector
from utilities.db_config import get_db_testing
import bcrypt

def signup():
    print("**Sign up Form**")
    full_name = input("Enter Full Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    phone_number = input("Enter Phone Number: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn = get_db_testing()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO login_details (full_name, username, password, phone_number) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (full_name, username, hashed_password, phone_number))
            conn.commit()
            print("Signup Successful! You can now login.")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            cursor.close()
            conn.close()