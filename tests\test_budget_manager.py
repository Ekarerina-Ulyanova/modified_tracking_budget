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
    result = budget_manager.add_expense(amount, category, description)

    # Assert
    assert result is True
    assert database.get_expenses() == [(1, amount, category, description)]

def test_remove_expense(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.remove_expense(0)

    # Assert
    assert result is True
    assert database.get_expenses() == []

def test_get_expense_amount(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.get_expense_amount(0)

    # Assert
    assert result == amount

def test_add_budget(budget_manager, database):
    # Arrange
    amount = 1000.0

    # Act
    result = budget_manager.add_budget(amount)

    # Assert
    assert result is True
    assert database.get_current_budget() == amount

def test_get_current_budget(budget_manager, database):
    # Arrange
    amount = 1000.0
    budget_manager.add_budget(amount)

    # Act
    result = budget_manager.get_current_budget()

    # Assert
    assert result == amount

def test_get_expenses(budget_manager, database):
    # Arrange
    amount1 = 100.0
    category1 = "Food"
    description1 = "Groceries"
    amount2 = 200.0
    category2 = "Transportation"
    description2 = "Gas"
    budget_manager.add_expense(amount1, category1, description1)
    budget_manager.add_expense(amount2, category2, description2)

    # Act
    result = budget_manager.get_expenses()

    # Assert
    assert result == ["$100.00 - Food: Groceries", "$200.00 - Transportation: Gas"]

def test_view_monthly_info(budget_manager, database):
    # Arrange
    amount1 = 100.0
    category1 = "Food"
    description1 = "Groceries"
    amount2 = 200.0
    category2 = "Transportation"
    description2 = "Gas"
    budget_manager.add_expense(amount1, category1, description1)
    budget_manager.add_expense(amount2, category2, description2)

    # Act
    result = budget_manager.view_monthly_info()

    # Assert
    assert result == {}

def test_clear_data(budget_manager, database):
    # Arrange
    amount1 = 100.0
    category1 = "Food"
    description1 = "Groceries"
    amount2 = 200.0
    category2 = "Transportation"
    description2 = "Gas"
    budget_manager.add_expense(amount1, category1, description1)
    budget_manager.add_expense(amount2, category2, description2)

    # Act
    budget_manager.clear_data()

    # Assert
    assert database.get_expenses() == []

def test_close(budget_manager, database):
    # Arrange
    amount1 = 100.0
    category1 = "Food"
    description1 = "Groceries"
    amount2 = 200.0
    category2 = "Transportation"
    description2 = "Gas"
    budget_manager.add_expense(amount1, category1, description1)
    budget_manager.add_expense(amount2, category2, description2)

    # Act
    budget_manager.close()

    # Assert
    assert database.is_closed() is True

def test_add_expense_invalid_amount(budget_manager, database):
    # Arrange
    amount = -100.0
    category = "Food"
    description = "Groceries"

    # Act
    result = budget_manager.add_expense(amount, category, description)

    # Assert
    assert result is False

def test_remove_expense_invalid_index(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.remove_expense(1)

    # Assert
    assert result is False

def test_get_expense_amount_invalid_index(budget_manager, database):
    # Arrange
    amount = 100.0
    category = "Food"
    description = "Groceries"
    budget_manager.add_expense(amount, category, description)

    # Act
    result = budget_manager.get_expense_amount(1)

    # Assert
    assert result == 0.0

def test_add_budget_invalid_amount(budget_manager, database):
    # Arrange
    amount = -1000.0

    # Act
    result = budget_manager.add_budget(amount)

    # Assert
    assert result is False

def test_get_current_budget_no_budget(budget_manager, database):
    # Act
    result = budget_manager.get_current_budget()

    # Assert
    assert result == 0.0

def test_get_expenses_no_expenses(budget_manager, database):
    # Act
    result = budget_manager.get_expenses()

    # Assert
    assert result == []

def test_view_monthly_info_no_data(budget_manager, database):
    # Act
    result = budget_manager.view_monthly_info()

    # Assert
    assert result == {}
```