from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GroceryList(Base):
    __tablename__ = 'grocery_lists'

    id = Column(Integer, primary_key=True)
    item = Column(String, nullable=False)
    quantity = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
