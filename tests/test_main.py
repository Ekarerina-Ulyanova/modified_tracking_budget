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
        budget_manager.add_category("Food", 100)
        budget_manager.add_category("Transportation", 50)
        budget_manager.add_expense("Food", 20)
        budget_manager.add_expense("Transportation", 30)
        assert budget_manager.get_total_budget() == 200
        assert budget_manager.get_total_expenses() == 50

    def test_database(self):
        """
        Test the Database class.
        """
        database = Database()
        database.add_record("2022-01-01", "Income", 1000)
        database.add_record("2022-01-02", "Expense", 500)
        assert database.get_total_income() == 1000
        assert database.get_total_expenses() == 500

def main():
    """
    Main function to run the tests.
    """
    test = TestMain()
    test.test_budget_manager()
    test.test_database()

if __name__ == "__main__":
    main()
```