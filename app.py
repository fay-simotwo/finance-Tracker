# Import necessary modules and classes
from models import User, Transaction, Goal, Investment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a database engine and a session
engine = create_engine('sqlite:///finance_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
