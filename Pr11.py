import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "a") as f:
        f.write(f"{username},{hash_password(password)}\n")
    print("Registration successful.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username and stored_hash == hash_password(password):
                print("Login successful.")
                return
    print("Invalid username or password.")

def main():
    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break

if not os.path.exists("users.txt"):
    open("users.txt", "w").close()

main()
