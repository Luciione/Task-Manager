# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship



Base = declarative_base()

class GroceryList(Base):
    __tablename__ = 'grocery_lists'

    id = Column(Integer, primary_key=True)
    item = Column(String, nullable=False)
    quantity = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


      # Define the foreign key relationship to the Reminder model
    reminder_id = Column(Integer, ForeignKey('reminders.id'))

    # Establish a relationship to the Reminder model
    reminder = relationship('Reminder', back_populates='notes')

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

# Create an SQLAlchemy engine and initialize the database
engine = create_engine('sqlite:///task_manager.db')
Base.metadata.create_all(engine)
