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

def test_add_expense(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"

    # Act
    budget_manager.db = database
    result = budget_manager.add_expense(amount, category, description)

    # Assert
    assert result is None

def test_remove_expense(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.db = database
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.remove_expense(0)

    # Assert
    assert result is True

def test_remove_expense_out_of_range(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act
    result = budget_manager.remove_expense(0)

    # Assert
    assert result is False

def test_get_expense_amount(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.db = database
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.get_expense_amount(0)

    # Assert
    assert result == amount

def test_get_expense_amount_out_of_range(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act
    result = budget_manager.get_expense_amount(0)

    # Assert
    assert result == 0.0

def test_add_budget(budget_manager, database):
    # Arrange
    amount = 1000.0

    # Act
    budget_manager.db = database
    result = budget_manager.add_budget(amount)

    # Assert
    assert result is None

def test_get_current_budget(budget_manager, database):
    # Arrange
    budget_manager.db = database
    budget_manager.add_budget(1000.0)

    # Act
    result = budget_manager.get_current_budget()

    # Assert
    assert result == 1000.0

def test_get_expenses(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.db = database
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.get_expenses()

    # Assert
    assert result == ["$100.00 - Food: Groceries"]

def test_view_monthly_info(budget_manager, database):
    # Arrange
    budget_manager.db = database
    budget_manager.add_budget(1000.0)
    budget_manager.add_expense(100.0, "Food", "Groceries")

    # Act
    result = budget_manager.view_monthly_info()

    # Assert
    assert result is not None

def test_clear_data(budget_manager, database):
    # Arrange
    budget_manager.db = database
    budget_manager.add_budget(1000.0)
    budget_manager.add_expense(100.0, "Food", "Groceries")

    # Act
    budget_manager.clear_data()

    # Assert
    assert budget_manager.db.get_expenses() == []

def test_close(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act
    result = budget_manager.close()

    # Assert
    assert result is None
```