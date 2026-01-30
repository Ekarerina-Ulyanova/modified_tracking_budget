import unittest
from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_connect(self):
        self.db.connect()
        self.assertTrue(self.db.is_connected)

    def test_disconnect(self):
        self.db.connect()
        self.db.disconnect()
        self.assertFalse(self.db.is_connected)

    def test_insert(self):
        self.db.connect()
        self.db.insert('test_table', {'id': 1, 'name': 'Test'})
        self.assertTrue(self.db.is_connected)

    def test_query(self):
        self.db.connect()
        result = self.db.query('SELECT * FROM test_table')
        self.assertIsInstance(result, list)

    def test_close(self):
        self.db.connect()
        self.db.close()
        self.assertFalse(self.db.is_connected)

if __name__ == '__main__':
    unittest.main()