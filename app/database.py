from sqlalchemy import create_engine


DATABASE_URL = 'sqlite:///task_manager.db'


engine = create_engine(DATABASE_URL)
