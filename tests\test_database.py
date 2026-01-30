```python
import pytest
import sqlite3
from database import Database

@pytest.fixture
def db():
    db = Database()
    yield db
    db.close()

def test_create_tables(db):
    # Arrange
    # Act
    db.create_tables()
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 2

def test_create_tables_existing_tables(db):
    # Arrange
    db.create_tables()
    # Act
    db.create_tables()
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 2

def test_add_expense(db):
    # Arrange
    # Act
    db.add_expense(10.99, "Food", "Lunch")
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"

def test_add_expense_duplicate(db):
    # Arrange
    db.add_expense(10.99, "Food", "Lunch")
    # Act
    db.add_expense(10.99, "Food", "Lunch")
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1

def test_remove_expense(db):
    # Arrange
    db.add_expense(10.99, "Food", "Lunch")
    # Act
    db.remove_expense(1)
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_remove_expense_non_existent(db):
    # Arrange
    # Act
    db.remove_expense(1)
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_add_budget(db):
    # Arrange
    db.add_budget(10.99)
    # Act
    current_budget = db.get_current_budget()
    # Assert
    assert current_budget == 10.99

def test_add_budget_zero(db):
    # Arrange
    db.add_budget(0)
    # Act
    current_budget = db.get_current_budget()
    # Assert
    assert current_budget == 0

def test_get_current_budget(db):
    # Arrange
    db.add_budget(10.99)
    # Act
    current_budget = db.get_current_budget()
    # Assert
    assert current_budget == 10.99

def test_get_expenses(db):
    # Arrange
    db.add_expense(10.99, "Food", "Lunch")
    # Act
    expenses = db.get_expenses()
    # Assert
    assert len(expenses) == 1
    assert expenses[0][0] == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"

def test_view_monthly_info(db):
    # Arrange
    db.add_expense(10.99, "Food", "Lunch")
    # Act
    info = db.view_monthly_info()
    # Assert
    assert "Total Expenses: $10.99" in info
    assert "10.99 - Food: Lunch" in info

def test_view_monthly_info_no_expenses(db):
    # Arrange
    # Act
    info = db.view_monthly_info()
    # Assert
    assert "Total Expenses: $0.00" in info

def test_clear(db):
    # Arrange
    db.add_expense(10.99, "Food", "Lunch")
    # Act
    db.clear()
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_clear_existing_tables(db):
    # Arrange
    db.create_tables()
    # Act
    db.clear()
    # Assert
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 0

def test_close(db):
    # Arrange
    # Act
    db.close()
    # Assert
    with pytest.raises(sqlite3.Error):
        db.connection.cursor()
```