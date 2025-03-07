from utilities import app_config


def login():
    print("***Login Form***")
    while True:
        entered_username = input("Enter Your username: ")
        entered_password = input("Enter Your Password: ")

        if entered_username != app_config.username and entered_password != app_config.password:
            print("Both Username and Password are incorrect")
        elif entered_username != app_config.username:
            print("Username is Incorrect")
        elif entered_password != app_config.password:
            print("Password is Incorrect")
        else:
            print(f"Login Successfully! Welcome {app_config.full_name}")
            break