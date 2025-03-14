from signup_form import signup
from login_form import login
from reset_password import reset_password
from logout import logout

def main():
    print("\n Welcome ")
    while True:
        choice_var = input("Do You Already Have an Account? Y/n: ").strip().lower()
        if choice_var == "y":
            failed_attempts = login()
            if failed_attempts >= 3:
                print("You have entered the wrong password too many times!")
                reset_password()
            else:
                logout()
            break

        elif choice_var == "n":
            print("Please Signup First!")
            signup()
            login()
            logout()
            break

        else:
            print("Invalid Selection, Try Again")
if __name__ == '__main__':
    main()