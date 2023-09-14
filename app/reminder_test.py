import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from reminder import Reminder, Base  # Import the Reminder class and Base from your application

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

class TestReminder(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database and tables
        Base.metadata.create_all(engine)
        self.session = Session()
        
        # Clear all reminders in the database
        self.session.query(Reminder).delete()
        self.session.commit()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_add_reminder(self):
        # Test adding a reminder
        title = 'Meeting'
        description = 'Team meeting'
        due_date = '2023-10-01 14:00:00'

        reminder = Reminder(title=title, description=description, due_date=due_date)
        self.session.add(reminder)
        self.session.commit()

        result = self.session.query(Reminder).filter_by(title=title).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.title, title)

    def test_list_reminders_empty(self):
        # Test listing reminders when the database is empty
        reminders = self.session.query(Reminder).all()
        self.assertEqual(len(reminders), 0)

    def test_update_reminder(self):
        # Test updating a reminder
        title = 'Original Title'
        new_title = 'Updated Title'
        description = 'Original Description'
        new_description = 'Updated Description'
        due_date = '2023-10-01 14:00:00'
        new_due_date = '2023-10-02 10:00:00'

        reminder = Reminder(title=title, description=description, due_date=due_date)
        self.session.add(reminder)
        self.session.commit()

        # Update the reminder
        reminder_to_update = self.session.query(Reminder).filter_by(title=title).first()
        reminder_to_update.title = new_title
        reminder_to_update.description = new_description
        reminder_to_update.due_date = new_due_date
        self.session.commit()

        updated_reminder = self.session.query(Reminder).filter_by(title=new_title).first()
        self.assertIsNotNone(updated_reminder)
        self.assertEqual(updated_reminder.title, new_title)
        self.assertEqual(updated_reminder.description, new_description)
        self.assertEqual(updated_reminder.due_date, new_due_date)

    def test_delete_reminder(self):
        # Test deleting a reminder
        title = 'Reminder to Delete'
        description = 'Description for Reminder to Delete'
        due_date = '2023-10-01 14:00:00'

        reminder = Reminder(title=title, description=description, due_date=due_date)
        self.session.add(reminder)
        self.session.commit()

        reminder_to_delete = title
        reminder_to_delete_query = self.session.query(Reminder).filter_by(title=reminder_to_delete).first()
        self.assertIsNotNone(reminder_to_delete_query)

        # Delete the reminder
        self.session.delete(reminder_to_delete_query)
        self.session.commit()

        deleted_reminder = self.session.query(Reminder).filter_by(title=reminder_to_delete).first()
        self.assertIsNone(deleted_reminder)

if __name__ == '__main__':
    unittest.main()
