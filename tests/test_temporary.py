import unittest
import tempfile
import os

class TemporaryFileTest(unittest.TestCase):
    def test_temporary_file(self):
        with tempfile.NamedTemporaryFile() as f:
            self.assertIsNotNone(f.name)
            self.assertTrue(os.path.exists(f.name))
            f.close()
            self.assertFalse(os.path.exists(f.name))

    def test_temporary_directory(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNotNone(d)
            self.assertTrue(os.path.exists(d))
            self.assertTrue(os.path.isdir(d))
            os.rmdir(d)
            self.assertFalse(os.path.exists(d))

if __name__ == '__main__':
    unittest.main()