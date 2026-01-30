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
    assert 'expenses' in [table[0] for table in tables]
    assert 'budget' in [table[0] for table in tables]

def test_add_expense(db):
    db.add_expense(10.99, 'Food', 'Lunch')
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == 'Food'
    assert expenses[0][3] == 'Lunch'

def test_remove_expense(db):
    db.add_expense(10.99, 'Food', 'Lunch')
    db.remove_expense(1)
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_add_budget(db):
    db.add_budget(100.00)
    assert db.get_current_budget() == 100.00

def test_get_current_budget(db):
    db.add_budget(100.00)
    assert db.get_current_budget() == 100.00

def test_get_expenses(db):
    db.add_expense(10.99, 'Food', 'Lunch')
    db.add_expense(20.00, 'Transportation', 'Gas')
    expenses = db.get_expenses()
    assert len(expenses) == 2
    assert expenses[0][0] == 1
    assert expenses[0][1] == 10.99
    assert expenses[0][2] == 'Food'
    assert expenses[0][3] == 'Lunch'
    assert expenses[1][0] == 2
    assert expenses[1][1] == 20.00
    assert expenses[1][2] == 'Transportation'
    assert expenses[1][3] == 'Gas'

def test_view_monthly_info(db):
    db.add_expense(10.99, 'Food', 'Lunch')
    db.add_expense(20.00, 'Transportation', 'Gas')
    info = db.view_monthly_info()
    assert "Total Expenses: $30.99" in info
    assert "10.99 - Food: Lunch" in info
    assert "20.00 - Transportation: Gas" in info

def test_clear(db):
    db.add_expense(10.99, 'Food', 'Lunch')
    db.clear()
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    assert len(expenses) == 0

def test_close(db):
    db.close()
    with pytest.raises(sqlite3.Error):
        db.connection.cursor()
```