from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import  classes from their respective files
from grocery_list import GroceryList
from reminder import Reminder
from note import Note

# Create an SQLAlchemy engine
engine = create_engine('sqlite:///task_manager.db')

# Initialize the database
Base.metadata.create_all(engine)
