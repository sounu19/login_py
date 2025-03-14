import mysql.connector
from utilities.db_config import get_db_testing

def logout():
    print("*** Logout ***")

    username = input("Enter your username to logout: ")

    conn = get_db_testing()
    if not conn:
        print("Database connection failed!")
        return

    try:
        cursor = conn.cursor()

        # Check if the user is logged in (has a session token)
        check_query = "SELECT session_token FROM login_details WHERE username = %s AND session_token IS NOT NULL"
        cursor.execute(check_query, (username,))
        result = cursor.fetchone()

        if result:
            # Invalidate the session
            update_query = "UPDATE login_details SET session_token = NULL, session_time = NULL WHERE username = %s"
            cursor.execute(update_query, (username,))
            conn.commit()

            print("Logout successful! Session has been destroyed.")
        else:
            print("No active session found for this user.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()
