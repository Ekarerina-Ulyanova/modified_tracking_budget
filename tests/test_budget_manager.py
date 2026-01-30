import unittest
from budget_manager import BudgetManager
from database import Database

class TestBudgetManager(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.budget_manager = BudgetManager(self.db)

    def test_create_budget(self):
        budget_name = "Test Budget"
        budget_amount = 1000
        self.budget_manager.create_budget(budget_name, budget_amount)
        self.assertTrue(self.db.get_budget(budget_name))

    def test_get_budget(self):
        budget_name = "Test Budget"
        budget_amount = 1000
        self.budget_manager.create_budget(budget_name, budget_amount)
        budget = self.budget_manager.get_budget(budget_name)
        self.assertEqual(budget['name'], budget_name)
        self.assertEqual(budget['amount'], budget_amount)

    def test_update_budget(self):
        budget_name = "Test Budget"
        budget_amount = 1000
        self.budget_manager.create_budget(budget_name, budget_amount)
        new_amount = 2000
        self.budget_manager.update_budget(budget_name, new_amount)
        budget = self.budget_manager.get_budget(budget_name)
        self.assertEqual(budget['amount'], new_amount)

    def test_delete_budget(self):
        budget_name = "Test Budget"
        budget_amount = 1000
        self.budget_manager.create_budget(budget_name, budget_amount)
        self.budget_manager.delete_budget(budget_name)
        self.assertFalse(self.db.get_budget(budget_name))

if __name__ == '__main__':
    unittest.main()