import random
import string
import hashlib

passwords = {}

def generate_password(length=12):
    """Generate a strong random password."""
    # Use uppercase, lowercase, digits, and special characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Shuffle the characters and pick the first `length` ones
    password = ''.join(random.sample(chars, length))
    return password

def hash_password(password):
    """Hash a password using SHA-256."""
    hash_obj = hashlib.sha256(password.encode())
    return hash_obj.hexdigest()

def save_password(username, password):
    """Save a hashed password for a given username."""
    hashed_password = hash_password(password)
    passwords[username] = hashed_password

def update_password(username):
    """Update the password for a given username."""
    print(f"Current password for {username}: {passwords[username]}")
    new_password = input("Enter a new password: ")
    save_password(username, new_password)

def main():
    """Main program loop."""
    while True:
        print("\n1. Generate a new password")
        print("2. Update an existing password")
        print("3. Quit")
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            username = input("Enter a username: ")
            password = generate_password()
            save_password(username, password)
            print(f"New password for {username}: {password}")
            
        elif choice == '2':
            username = input("Enter a username: ")
            if username in passwords:
                update_password(username)
            else:
                print("Username not found.")
            
        elif choice == '3':
            break
            
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
