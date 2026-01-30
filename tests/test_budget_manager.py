```python
from budget_manager import BudgetManager
from database import Database

class TestBudgetManager:
    """
    Test class for BudgetManager.
    """

    def test_init(self):
        """
        Test the initialization of BudgetManager.
        """
        budget_manager = BudgetManager()
        assert budget_manager is not None

    def test_add_budget(self):
        """
        Test adding a budget to the BudgetManager.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        assert budget_manager.get_budget("rent") == 1000

    def test_remove_budget(self):
        """
        Test removing a budget from the BudgetManager.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        budget_manager.remove_budget("rent")
        assert budget_manager.get_budget("rent") is None

    def test_update_budget(self):
        """
        Test updating a budget in the BudgetManager.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        budget_manager.update_budget("rent", 1200)
        assert budget_manager.get_budget("rent") == 1200

    def test_get_budget(self):
        """
        Test getting a budget from the BudgetManager.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        assert budget_manager.get_budget("rent") == 1000

    def test_get_all_budgets(self):
        """
        Test getting all budgets from the BudgetManager.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        budget_manager.add_budget("electricity", 50)
        assert budget_manager.get_all_budgets() == {"rent": 1000, "electricity": 50}

    def test_save_budgets(self):
        """
        Test saving budgets to the database.
        """
        budget_manager = BudgetManager()
        budget_manager.add_budget("rent", 1000)
        budget_manager.save_budgets()
        database = Database()
        assert database.get_budgets() == {"rent": 1000}

    def test_load_budgets(self):
        """
        Test loading budgets from the database.
        """
        database = Database()
        database.save_budgets({"rent": 1000})
        budget_manager = BudgetManager()
        budget_manager.load_budgets()
        assert budget_manager.get_budget("rent") == 1000

if __name__ == "__main__":
    test = TestBudgetManager()
    test.test_init()
    test.test_add_budget()
    test.test_remove_budget()
    test.test_update_budget()
    test.test_get_budget()
    test.test_get_all_budgets()
    test.test_save_budgets()
    test.test_load_budgets()
```