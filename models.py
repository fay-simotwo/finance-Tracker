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