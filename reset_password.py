import mysql.connector
from utilities.db_config import get_db_testing
import bcrypt


def reset_password():
    print("*** Password Reset ***")

    username = input("Enter your username: ")
    phone_number = input("Enter your registered phone number: ")

    conn = get_db_testing()
    if not conn:
        print("Database connection failed!")
        return

    try:
        cursor = conn.cursor()
        query = "SELECT full_name FROM login_details WHERE username = %s AND phone_number = %s"
        cursor.execute(query, (username, phone_number))
        result = cursor.fetchone()

        if result:
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")

            if new_password == confirm_password:
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                update_query = "UPDATE login_details SET password = %s WHERE username = %s"
                cursor.execute(update_query, (hashed_password, username))
                conn.commit()

                print("Password successfully reset! You can now log in.")
            else:
                print("Passwords do not match. Try again.")
        else:
            print("User not found or incorrect phone number.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()
