import unittest
from app.controllers.item_controller import ItemController
from app.models.item import Item

class TestItemController(unittest.TestCase):

    def setUp(self):
        self.controller = ItemController()
        self.test_item = Item(id=1, name="Test Item", description="This is a test item.")

    def test_create_item(self):
        result = self.controller.create_item(self.test_item)
        self.assertTrue(result)
        self.assertIn(self.test_item, self.controller.get_all_items())

    def test_read_item(self):
        self.controller.create_item(self.test_item)
        item = self.controller.read_item(self.test_item.id)
        self.assertEqual(item.name, self.test_item.name)

    def test_update_item(self):
        self.controller.create_item(self.test_item)
        updated_item = Item(id=1, name="Updated Item", description="This is an updated test item.")
        result = self.controller.update_item(updated_item)
        self.assertTrue(result)
        item = self.controller.read_item(updated_item.id)
        self.assertEqual(item.name, updated_item.name)

    def test_delete_item(self):
        self.controller.create_item(self.test_item)
        result = self.controller.delete_item(self.test_item.id)
        self.assertTrue(result)
        self.assertNotIn(self.test_item, self.controller.get_all_items())

if __name__ == '__main__':
    unittest.main()