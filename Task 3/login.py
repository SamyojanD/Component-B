from password_manager import find_user, load_users, encrypt_password

def main():
    print("Login")
    print("-----\n")
    username = input("User     :")
    password = input("Password :")

    users = load_users()
    user = find_user(users, username)

    if user and user[2] == encrypt_password(password):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
