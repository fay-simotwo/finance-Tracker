# Import necessary modules and classes
from models import User, Transaction, Goal, Investment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database engine and a session
engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()


# Function to create a new user
def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    # Create a User object
    user = User(username=username, password=password, email=email)

    # Add the user to the session and commit to save it to the database
    session.add(user)
    session.commit()
    print(f"User {username} created.")

 # Function to list all users
def list_users():
    # Query all users from the database
    users = session.query(User).all()
    
    # Display user information
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

# Main function
def main():
    while True:
        print("Options:")
        print("1. Create User")
        print("2. List Users")
        print("3. Quit")

        # Get user input for the desired action
        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")        