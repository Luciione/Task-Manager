import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from note import Note, Base  

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

class TestNote(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database and tables
        Base.metadata.create_all(engine)
        self.session = Session()
        
        # Clear all notes in the database
        self.session.query(Note).delete()
        self.session.commit()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_add_note(self):
        # Test adding a note
        content = 'This is a test note'
        note = Note(content=content)
        self.session.add(note)
        self.session.commit()

        result = self.session.query(Note).filter_by(content=content).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.content, content)

    def test_list_notes_empty(self):
        # Test listing notes when the database is empty
        notes = self.session.query(Note).all()
        self.assertEqual(len(notes), 0)

    def test_update_note(self):
        # Test updating a note
        content = 'Original content'
        new_content = 'Updated content'

        note = Note(content=content)
        self.session.add(note)
        self.session.commit()

        # Update the content of the note
        note_to_update = self.session.query(Note).filter_by(content=content).first()
        note_to_update.content = new_content
        self.session.commit()

        updated_note = self.session.query(Note).filter_by(content=new_content).first()
        self.assertIsNotNone(updated_note)
        self.assertEqual(updated_note.content, new_content)

    def test_delete_note(self):
        # Test deleting a note
        content = 'Note to delete'

        note = Note(content=content)
        self.session.add(note)
        self.session.commit()

        note_to_delete = content
        note_to_delete_query = self.session.query(Note).filter_by(content=note_to_delete).first()
        self.assertIsNotNone(note_to_delete_query)

        # Delete the note
        self.session.delete(note_to_delete_query)
        self.session.commit()

        deleted_note = self.session.query(Note).filter_by(content=note_to_delete).first()
        self.assertIsNone(deleted_note)

if __name__ == '__main__':
    unittest.main()
