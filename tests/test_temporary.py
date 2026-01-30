import unittest
from unittest.mock import patch
from tempfile import TemporaryDirectory
from budget_manager import BudgetManager

class TestTemporaryDirectory(unittest.TestCase):

    def test_temporary_directory(self):
        with TemporaryDirectory() as temp_dir:
            self.assertEqual(temp_dir, TemporaryDirectory().name)

    @patch('budget_manager.BudgetManager')
    def test_budget_manager(self, mock_budget_manager):
        with TemporaryDirectory() as temp_dir:
            budget_manager = BudgetManager(temp_dir)
            self.assertIsInstance(budget_manager, BudgetManager)

if __name__ == '__main__':
    unittest.main()