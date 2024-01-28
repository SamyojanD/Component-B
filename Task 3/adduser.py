from password_manager import add_user

def main():
    print("Add User")
    print("--------\n")
    username = input("Enter new username: ")
    real_name = input("Enter real name   : ")
    password = input("Enter password    : ")
    add_user(username, real_name, password)

if __name__ == "__main__":
    main()
