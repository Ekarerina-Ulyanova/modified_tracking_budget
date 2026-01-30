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
    budget_manager.db = database
    amount = 100.0
    category = "Food"
    description = "Groceries"

    # Act
    budget_manager.add_expense(amount, category, description)

    # Assert
    expenses = database.get_expenses()
    assert len(expenses) == 1
    assert expenses[0][1] == amount
    assert expenses[0][2] == category
    assert expenses[0][3] == description

def test_remove_expense(budget_manager, database):
    # Arrange
    budget_manager.db = database
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    budget_manager.remove_expense(0)

    # Assert
    expenses = database.get_expenses()
    assert len(expenses) == 0

def test_remove_expense_out_of_range(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act and Assert
    with pytest.raises(IndexError):
        budget_manager.remove_expense(0)

def test_get_expense_amount(budget_manager, database):
    # Arrange
    budget_manager.db = database
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    expense_amount = budget_manager.get_expense_amount(0)

    # Assert
    assert expense_amount == amount

def test_get_expense_amount_out_of_range(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act and Assert
    with pytest.raises(IndexError):
        budget_manager.get_expense_amount(0)

def test_add_budget(budget_manager, database):
    # Arrange
    budget_manager.db = database
    amount = 1000.0

    # Act
    budget_manager.add_budget(amount)

    # Assert
    budget = database.get_current_budget()
    assert budget == amount

def test_get_current_budget(budget_manager, database):
    # Arrange
    budget_manager.db = database
    budget_manager.add_budget(1000.0)

    # Act
    current_budget = budget_manager.get_current_budget()

    # Assert
    assert current_budget == 1000.0

def test_get_expenses(budget_manager, database):
    # Arrange
    budget_manager.db = database
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    expenses = budget_manager.get_expenses()

    # Assert
    assert len(expenses) == 1
    assert expenses[0] == f"${amount:.2f} - {category}: {description}"

def test_view_monthly_info(budget_manager):
    # Act and Assert
    budget_manager.view_monthly_info()

def test_clear_data(budget_manager, database):
    # Arrange
    budget_manager.db = database
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    budget_manager.clear_data()

    # Assert
    expenses = database.get_expenses()
    assert len(expenses) == 0

def test_close(budget_manager, database):
    # Arrange
    budget_manager.db = database

    # Act
    budget_manager.close()

    # Assert
    assert database.is_closed()
```