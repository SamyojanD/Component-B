import hashlib

PASSWORD_FILE = "passwd.txt"

def load_users():
    with open(PASSWORD_FILE, "r") as file:
        lines = file.readlines()
    return [line.strip().split(":") for line in lines]

def save_users(users):
    with open(PASSWORD_FILE, "w") as file:
        for user in users:
            file.write(":".join(user) + "\n")

def find_user(users, username):
    for user in users:
        if user[0] == username:
            return user
    return None

def encrypt_password(password):
    # SHA-256 hashing
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, real_name, password):
    users = load_users()
    if find_user(users, username):
        print("The username most likely already exists. Cannot add.")
        return False

    encrypted_password = encrypt_password(password)
    users.append([username, real_name, encrypted_password])
    save_users(users)
    print("User Created.")
    return True

def del_user(username):
    users = load_users()
    user = find_user(users, username)
    if user:
        users.remove(user)
        save_users(users)
        print("User Deleted.")
        return True
    else:
        print("User not found. Nothing deleted.")
        return False

def change_password(username, current_password, new_password):
    users = load_users()
    user = find_user(users, username)
    if user and user[2] == encrypt_password(current_password):
        user[2] = encrypt_password(new_password)
        save_users(users)
        print("Password changed.")
        return True
    else:
        print("Invalid username or password. Nothing changed.")
        return False
