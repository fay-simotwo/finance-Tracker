# Import necessary modules and classes from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy base class
Base = declarative_base()

# Define the User table
class User(Base):
    __tablename__ = 'users'

    # Define columns for the User table
    id = Column(Integer, primary_key=True)        # Unique identifier
    username = Column(String, unique=True, nullable=False)  # Username (unique)
    password = Column(String, nullable=False)      # Password
    email = Column(String, unique=True, nullable=False)     # Email address

    # Define relationships between User and other tables
    transactions = relationship('Transaction', back_populates='user')
    goals = relationship('Goal', back_populates='user')
    investments = relationship('Investment', back_populates='user')

    # Define the Transaction table
class Transaction(Base):
    __tablename__ = 'transactions'

    # Define columns for the Transaction table
    id = Column(Integer, primary_key=True)    # Unique identifier
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # User ID (foreign key)
    date = Column(Date, nullable=False)       # Transaction date
    description = Column(String, nullable=False)   # Description of the transaction
    amount = Column(Float, nullable=False)    # Transaction amount
    transaction_type = Column(String, nullable=False)   # Transaction type (Income or Expense)

    # Define the relationship between Transaction and User
    user = relationship('User', back_populates='transactions')

    # Define the Goal table
class Goal(Base):
    __tablename__ = 'goals'

    # Define columns for the Goal table
    id = Column(Integer, primary_key=True)    # Unique identifier
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # User ID (foreign key)
    name = Column(String, nullable=False)     # Goal name
    target_amount = Column(Float, nullable=False)   # Target amount
    current_amount = Column(Float, nullable=False)  # Current amount saved
    target_date = Column(Date)                 # Target date (optional)

    # Define the relationship between Goal and User
    user = relationship('User', back_populates='goals')

    # Define the Investment table
class Investment(Base):
    __tablename__ = 'investments'

    # Define columns for the Investment table
    id = Column(Integer, primary_key=True)    # Unique identifier
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # User ID (foreign key)
    name = Column(String, nullable=False)     # Investment name
    amount_invested = Column(Float, nullable=False)  # Amount invested
    current_value = Column(Float, nullable=False)   # Current value of the investment
    purchase_date = Column(Date, nullable=False)     # Purchase date

    # Define the relationship between Investment and User
    user = relationship('User', back_populates='investments')