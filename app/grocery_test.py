import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from grocery_list import GroceryList, Base  


engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

class TestGroceryList(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database and tables
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_add_grocery(self):
        # Test adding an item to the grocery list
        item = GroceryList(item='Tomatoes', quantity=50)
        self.session.add(item)
        self.session.commit()
    
        result = self.session.query(GroceryList).filter_by(item='Tomatoes').first()  
        self.assertIsNotNone(result)
        self.assertEqual(result.item, 'Tomatoes')

    def test_list_grocery_empty(self):
        # Test listing items in an empty grocery list
        items = self.session.query(GroceryList).all()
        self.assertEqual(len(items), 0)

    def test_update_grocery(self):
        # Test updating an item in the grocery list
        item = GroceryList(item='Apples', quantity=3)
        self.session.add(item)
        self.session.commit()

        # Update the quantity of 'Apples'
        updated_quantity = 5
        item_to_update = self.session.query(GroceryList).filter_by(item='Apples').first()
        item_to_update.quantity = updated_quantity
        self.session.commit()

        updated_item = self.session.query(GroceryList).filter_by(item='Apples').first()
        self.assertEqual(updated_item.quantity, updated_quantity)

    def test_delete_grocery(self):
        # Test deleting an item from the grocery list
        item = GroceryList(item='Bananas', quantity=4)
        self.session.add(item)
        self.session.commit()

        item_to_delete = 'Bananas'
        item_to_delete_query = self.session.query(GroceryList).filter_by(item=item_to_delete).first()
        self.assertIsNotNone(item_to_delete_query)

        # Delete the item
        self.session.delete(item_to_delete_query)
        self.session.commit()

        deleted_item = self.session.query(GroceryList).filter_by(item=item_to_delete).first()
        self.assertIsNone(deleted_item)

if __name__ == '__main__':
    unittest.main()
