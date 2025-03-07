from utilities import app_config


def signup():
    print("**Sign up Form**")
    app_config.full_name = input("Enter Full Name: ")
    app_config.username = input("Enter Username: ")
    app_config.password = input("Enter Password: ")
    print("Signup successful! You can now log in.")
