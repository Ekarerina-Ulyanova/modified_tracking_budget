import unittest
from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_create_table(self):
        self.db.create_table('test_table', ['id', 'name'])
        self.assertTrue(self.db.table_exists('test_table'))

    def test_insert_data(self):
        self.db.insert_data('test_table', {'id': 1, 'name': 'John'})
        self.assertTrue(self.db.row_exists('test_table', 1))

    def test_select_data(self):
        self.db.insert_data('test_table', {'id': 1, 'name': 'John'})
        result = self.db.select_data('test_table', 'name', 'id = 1')
        self.assertEqual(result[0][0], 'John')

    def test_update_data(self):
        self.db.insert_data('test_table', {'id': 1, 'name': 'John'})
        self.db.update_data('test_table', {'name': 'Jane'}, 'id = 1')
        result = self.db.select_data('test_table', 'name', 'id = 1')
        self.assertEqual(result[0][0], 'Jane')

    def test_delete_data(self):
        self.db.insert_data('test_table', {'id': 1, 'name': 'John'})
        self.db.delete_data('test_table', 'id = 1')
        self.assertFalse(self.db.row_exists('test_table', 1))

if __name__ == '__main__':
    unittest.main()