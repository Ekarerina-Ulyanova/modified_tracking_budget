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
    db.add_expense(10.99, "Food", "Lunch")
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"

def test_remove_expense(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Lunch")
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
    db.add_expense(10.99, "Food", "Lunch")
    expenses = db.get_expenses()
    assert len(expenses) == 1
    assert expenses[0][0] == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"

def test_view_monthly_info(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Lunch")
    info = db.view_monthly_info()
    assert "Total Expenses: $10.99" in info
    assert "10.99 - Food: Lunch" in info

def test_clear(db):
    db.create_tables()
    db.add_expense(10.99, "Food", "Lunch")
    db.clear()
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_close(db):
    db.close()
    with pytest.raises(sqlite3.OperationalError):
        db.connection.cursor()

def test_add_expense_negative_amount(db):
    db.create_tables()
    with pytest.raises(ValueError):
        db.add_expense(-10.99, "Food", "Lunch")

def test_add_budget_negative_amount(db):
    db.create_tables()
    with pytest.raises(ValueError):
        db.add_budget(-10.99)

def test_remove_expense_non_existent_id(db):
    db.create_tables()
    with pytest.raises(ValueError):
        db.remove_expense(1)

def test_get_current_budget_non_existent_budget(db):
    db.create_tables()
    with pytest.raises(ValueError):
        db.get_current_budget()

def test_get_expenses_non_existent_expenses(db):
    db.create_tables()
    assert db.get_expenses() == []

def test_view_monthly_info_non_existent_expenses(db):
    db.create_tables()
    assert db.view_monthly_info() == "Total Expenses: $0.00\n"
```