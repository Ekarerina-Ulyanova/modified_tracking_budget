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
    db.create_tables()
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 2
    assert "expenses" in [table[0] for table in tables]
    assert "budget" in [table[0] for table in tables]

def test_add_expense(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Groceries")
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Groceries"

def test_remove_expense(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Groceries")
    db.remove_expense(1)
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_add_budget(db):
    db.create_tables()
    db.add_budget(10.99)
    cursor = db.connection.cursor()
    cursor.execute("SELECT amount FROM budget WHERE id = 1")
    budget = cursor.fetchone()[0]
    assert budget == 10.99

def test_get_current_budget(db):
    db.create_tables()
    db.add_budget(10.99)
    assert db.get_current_budget() == 10.99

def test_get_expenses(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Groceries")
    expenses = db.get_expenses()
    assert len(expenses) == 1
    assert expenses[0][0] == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Groceries"

def test_view_monthly_info(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Groceries")
    info = db.view_monthly_info()
    assert "Total Expenses: $10.99" in info
    assert "10.99 - Food: Groceries" in info

def test_clear(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Groceries")
    db.clear()
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_close(db):
    db.close()
    with pytest.raises(sqlite3.Error):
        db.connection.cursor()

def test_add_expense_invalid_amount(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.add_expense("invalid", "Food", "Groceries")

def test_remove_expense_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.remove_expense("invalid")

def test_add_budget_invalid_amount(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.add_budget("invalid")

def test_get_current_budget_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.get_current_budget("invalid")

def test_get_expenses_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.get_expenses("invalid")

def test_view_monthly_info_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.view_monthly_info("invalid")

def test_clear_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.clear("invalid")

def test_close_invalid_id(db):
    db.create_tables()
    with pytest.raises(TypeError):
        db.close("invalid")
```