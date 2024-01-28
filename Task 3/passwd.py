from password_manager import change_password

def main():
    print("Change Password")
    print("================\n")
    username = input("User            : ")
    current_password = input("Current Password: ")
    new_password = input("New Password    : ")
    confirm_password = input("Confirm         : ")

    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match. Nothing changed.")

if __name__ == "__main__":
    main()
