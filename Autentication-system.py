import re
import hashlib
from datetime import datetime
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    strength = password_strength(password)
    
    if strength != "Strong password.":
        print(strength)
        return
    password = hash_password(password)    
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")
        print("Registration successful!")   
        time(f"User registered, {username}")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hash_password(password) == stored_password:
                print("Login successful!")
                time(f"User logged in, {username}")
                return username
    print("Invalid username or password. Please try again.")
    return None
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username is not None:
                        after_login(username)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")           
def password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    return "Strong password."
def time(event):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as file:
        file.write(f"{current_time} - {event}\n")
def logview(username):
    try:
        with open("log.txt", "r") as file:
            logs = file.readlines()
            user_logs = [log.strip() for log in logs if username in log]
            if user_logs:
                for log in user_logs:
                    print(log)
    except FileNotFoundError:
        print("Log file not found.")
def after_login(username):
    while True:
        print("1. View Logs")
        print("2. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            logview(username)
        elif choice == '2':
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")        
main()           

        


    




