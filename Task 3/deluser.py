from password_manager import del_user

def main():
    print("Delete User")
    print("------------\n")
    username = input("Enter username: ")
    del_user(username)

if __name__ == "__main__":
    main()
