# Import necessary modules and classes
from models import User, Transaction, Goal, Investment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database engine and a session
engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to populate the database with initial data
def seed_data():
    # Create sample users
    user1 = User(username='_hyper', password='password1', email='harps12@gmail.com')
    user2 = User(username='kay_kay', password='password2', email='kay2@gmail.com')

    # Create sample transactions
    transaction1 = Transaction(user=user1, date='2023-01-01', description='Salary', amount=50000, transaction_type='Income')
    transaction2 = Transaction(user=user1, date='2023-01-05', description='Groceries', amount=2000, transaction_type='Expense')
    transaction3 = Transaction(user=user2, date='2023-01-10', description='Rent', amount=8000, transaction_type='Expense')

    # Add the created objects to the session and commit to save them to the database
    session.add_all([user1, user2, transaction1, transaction2, transaction3])
    session.commit()

# Entry point of the script
if __name__ == '__main__':
    seed_data()
