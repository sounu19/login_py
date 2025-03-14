import mysql.connector
from utilities.db_config import get_db_testing
import bcrypt
import uuid
import datetime

def login():
    print("***Login Form***")

    conn = get_db_testing()
    if not conn:
        print("Database Connection Failed!")
        return 0

    failed_attempts = 0

    try:
        cursor = conn.cursor()

        while failed_attempts < 3:
            entered_username = input("Enter Your username: ")
            entered_password = input("Enter Your Password: ")

            query = "SELECT full_name, password, phone_number from login_details WHERE username = %s"
            cursor.execute(query, (entered_username,))
            result = cursor.fetchone()

            if result:
                full_name, stored_password, phone_number = result

                if bcrypt.checkpw(entered_password.encode('utf-8'), stored_password.encode('utf-8')):
                    print(f"Login Successfully! welcome {full_name}")

                    session_token = str(uuid.uuid4())
                    session_time = datetime.datetime.now()

                    update_query = "UPDATE login_details SET session_token = %s, session_time = %s WHERE username = %s"
                    cursor.execute(update_query, (session_token, session_time, entered_username))
                    conn.commit()

                    print(f"Session Started! Token: {session_token}")
                    return 0
                else:
                    print("Password is incorrect")
            else:
                print("Username is incorrect")
            failed_attempts += 1

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

    finally:
        cursor.close()
        conn.close()

    return  failed_attempts