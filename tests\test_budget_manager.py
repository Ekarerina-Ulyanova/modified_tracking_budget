```python
import pytest
from budget_manager import BudgetManager
from database import Database
from unittest.mock import Mock

@pytest.fixture
def budget_manager():
    return BudgetManager()

@pytest.fixture
def database():
    return Database()

def test_budget_manager_init(budget_manager):
    assert budget_manager.db is not None

def test_add_expense(budget_manager, database):
    database.add_expense = Mock(return_value=None)
    budget_manager.db = database
    budget_manager.add_expense(10.99, "Food", "Groceries")
    database.add_expense.assert_called_once_with(10.99, "Food", "Groceries")

def test_add_expense_negative_amount(budget_manager, database):
    database.add_expense = Mock(side_effect=Exception)
    budget_manager.db = database
    with pytest.raises(Exception):
        budget_manager.add_expense(-10.99, "Food", "Groceries")

def test_remove_expense(budget_manager, database):
    database.get_expenses = Mock(return_value=[(1, 10.99, "Food", "Groceries")])
    database.remove_expense = Mock(return_value=None)
    budget_manager.db = database
    budget_manager.remove_expense(0)
    database.remove_expense.assert_called_once_with(1)

def test_remove_expense_index_out_of_range(budget_manager, database):
    database.get_expenses = Mock(return_value=[(1, 10.99, "Food", "Groceries")])
    budget_manager.db = database
    with pytest.raises(IndexError):
        budget_manager.remove_expense(1)

def test_get_expense_amount(budget_manager, database):
    database.get_expenses = Mock(return_value=[(1, 10.99, "Food", "Groceries")])
    budget_manager.db = database
    assert budget_manager.get_expense_amount(0) == 10.99

def test_get_expense_amount_index_out_of_range(budget_manager, database):
    database.get_expenses = Mock(return_value=[(1, 10.99, "Food", "Groceries")])
    budget_manager.db = database
    with pytest.raises(IndexError):
        budget_manager.get_expense_amount(1)

def test_add_budget(budget_manager, database):
    database.add_budget = Mock(return_value=None)
    budget_manager.db = database
    budget_manager.add_budget(100.00)
    database.add_budget.assert_called_once_with(100.00)

def test_get_current_budget(budget_manager, database):
    database.get_current_budget = Mock(return_value=100.00)
    budget_manager.db = database
    assert budget_manager.get_current_budget() == 100.00

def test_get_expenses(budget_manager, database):
    database.get_expenses = Mock(return_value=[(1, 10.99, "Food", "Groceries")])
    budget_manager.db = database
    assert budget_manager.get_expenses() == ["$10.99 - Food: Groceries"]

def test_view_monthly_info(budget_manager, database):
    database.view_monthly_info = Mock(return_value={"month": "January", "year": 2022})
    budget_manager.db = database
    assert budget_manager.view_monthly_info() == {"month": "January", "year": 2022}

def test_clear_data(budget_manager, database):
    database.clear = Mock(return_value=None)
    budget_manager.db = database
    budget_manager.clear_data()
    database.clear.assert_called_once()

def test_close(budget_manager, database):
    database.close = Mock(return_value=None)
    budget_manager.db = database
    budget_manager.close()
    database.close.assert_called_once()
```