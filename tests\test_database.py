```python
import pytest
import sqlite3
from database import Database

@pytest.fixture
def db():
    db = Database()
    yield db
    db.close()

def test_init(db):
    assert db.connection is not None
    assert db.cursor is not None

def test_create_tables(db):
    db.create_tables()
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 2
    assert "expenses" in [table[0] for table in tables]
    assert "budget" in [table[0] for table in tables]

def test_add_expense(db):
    db.add_expense(10.99, "Food", "Lunch")
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"

def test_remove_expense(db):
    db.add_expense(10.99, "Food", "Lunch")
    db.remove_expense(1)
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_add_budget(db):
    db.add_budget(10.99)
    assert db.get_current_budget() == 10.99

def test_get_current_budget(db):
    db.add_budget(10.99)
    assert db.get_current_budget() == 10.99

def test_get_expenses(db):
    db.add_expense(10.99, "Food", "Lunch")
    db.add_expense(5.99, "Food", "Dinner")
    expenses = db.get_expenses()
    assert len(expenses) == 2
    assert expenses[0][0] == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == "Food"
    assert expenses[0][3] == "Lunch"
    assert expenses[1][0] == 2
    assert expenses[1][1] == 5.99
    assert expenses[1][2] == "Food"
    assert expenses[1][3] == "Dinner"

def test_view_monthly_info(db):
    db.add_expense(10.99, "Food", "Lunch")
    db.add_expense(5.99, "Food", "Dinner")
    info = db.view_monthly_info()
    assert info.startswith("Total Expenses: $16.98")
    assert "10.99 - Food: Lunch" in info
    assert "5.99 - Food: Dinner" in info

def test_clear(db):
    db.add_expense(10.99, "Food", "Lunch")
    db.clear()
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_close(db):
    db.close()
    with pytest.raises(sqlite3.Error):
        db.connection.cursor()

def test_add_expense_negative_amount(db):
    with pytest.raises(TypeError):
        db.add_expense(-10.99, "Food", "Lunch")

def test_add_budget_negative_amount(db):
    with pytest.raises(TypeError):
        db.add_budget(-10.99)

def test_get_current_budget_non_existent_budget(db):
    assert db.get_current_budget() == 0

def test_get_expenses_empty_table(db):
    assert db.get_expenses() == []

def test_view_monthly_info_empty_table(db):
    assert db.view_monthly_info() == ""

def test_clear_non_existent_table(db):
    db.clear()
    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) == 0

def test_close_non_existent_connection(db):
    db.close()
    with pytest.raises(sqlite3.Error):
        db.connection.cursor()
```