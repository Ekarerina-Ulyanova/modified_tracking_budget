```python
import pytest
from budget_manager import BudgetManager
from database import Database

@pytest.fixture
def budget_manager():
    return BudgetManager()

@pytest.fixture
def database():
    return Database()

def test_budget_manager_init(budget_manager):
    assert budget_manager.db is not None

def test_add_expense(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.db.get_expenses() == [(1, 100.0, "Food", "Groceries")]

def test_remove_expense(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    budget_manager.remove_expense(0)
    assert budget_manager.db.get_expenses() == []

def test_get_expense_amount(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.get_expense_amount(0) == 100.0

def test_add_budget(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_budget(1000.0)
    assert budget_manager.db.get_current_budget() == 1000.0

def test_get_current_budget(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_budget(1000.0)
    assert budget_manager.get_current_budget() == 1000.0

def test_get_expenses(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.get_expenses() == ["$100.00 - Food: Groceries"]

def test_view_monthly_info(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.view_monthly_info() == {}

def test_clear_data(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    budget_manager.clear_data()
    assert budget_manager.db.get_expenses() == []

def test_close(budget_manager, database):
    budget_manager.db = database
    budget_manager.close()
    assert budget_manager.db is None

def test_get_total_expenses(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.get_total_expenses() == 100.0

def test_get_average_expense(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    assert budget_manager.get_average_expense() == 100.0

def test_get_average_expense_zero_expenses(budget_manager, database):
    budget_manager.db = database
    assert budget_manager.get_average_expense() == 0.0

def test_get_average_expense_zero_total_expenses(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(0.0, "Food", "Groceries")
    assert budget_manager.get_average_expense() == 0.0

def test_get_average_expense_multiple_expenses(budget_manager, database):
    budget_manager.db = database
    budget_manager.add_expense(100.0, "Food", "Groceries")
    budget_manager.add_expense(200.0, "Food", "Groceries")
    assert budget_manager.get_average_expense() == 150.0
```