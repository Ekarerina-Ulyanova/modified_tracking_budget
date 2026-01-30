```python
from budget_manager import BudgetManager
from database import Database

class TestMain:
    """
    Test class for main functionality.
    """

    def test_budget_manager(self):
        """
        Test the BudgetManager class.
        """
        budget_manager = BudgetManager()
        budget_manager.add_category("Food", 1000)
        budget_manager.add_category("Transportation", 500)
        budget_manager.add_expense("Food", 200)
        budget_manager.add_expense("Transportation", 100)
        assert budget_manager.get_balance() == 1700

    def test_database(self):
        """
        Test the Database class.
        """
        database = Database()
        database.add_category("Food", 1000)
        database.add_category("Transportation", 500)
        database.add_expense("Food", 200)
        database.add_expense("Transportation", 100)
        assert database.get_balance() == 1700

def main():
    """
    Main function to run tests.
    """
    test = TestMain()
    test.test_budget_manager()
    test.test_database()

if __name__ == "__main__":
    main()
```