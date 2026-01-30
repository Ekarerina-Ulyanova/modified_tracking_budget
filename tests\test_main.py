```python
import pytest
import tkinter as tk
from tkinter import messagebox
from budget_manager import BudgetManager
from main import BudgetApp

@pytest.fixture
def mock_budget_manager():
    return BudgetManager()

@pytest.fixture
def mock_root():
    return tk.Tk()

def test_budget_app_init(mock_root):
    app = BudgetApp(mock_root)
    assert app.root == mock_root
    assert app.budget_manager == mock_budget_manager()

def test_create_widgets(mock_root):
    app = BudgetApp(mock_root)
    assert app.budget_label is not None
    assert app.budget_entry is not None
    assert app.add_budget_button is not None
    assert app.amount_entry is not None
    assert app.category_entry is not None
    assert app.description_entry is not None
    assert app.add_button is not None
    assert app.expense_listbox is not None
    assert app.remove_button is not None
    assert app.view_button is not None
    assert app.filter_button is not None
    assert app.filter_label is not None
    assert app.filter_entry is not None

def test_add_expense(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.amount_entry.insert(0, "100")
    app.category_entry.insert(0, "Test Category")
    app.description_entry.insert(0, "Test Description")
    app.add_button.invoke()
    assert app.budget_manager.get_current_budget() == 0
    assert app.budget_manager.get_expenses() == [("Test Category", "Test Description", 100)]

def test_add_expense_invalid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.amount_entry.insert(0, "abc")
    app.category_entry.insert(0, "Test Category")
    app.description_entry.insert(0, "Test Description")
    app.add_button.invoke()
    assert app.budget_manager.get_current_budget() == 0
    assert app.budget_manager.get_expenses() == []

def test_remove_expense(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.expense_listbox.insert(0, "Test Category, Test Description, 100")
    app.remove_button.invoke()
    assert app.budget_manager.get_current_budget() == 100
    assert app.budget_manager.get_expenses() == []

def test_remove_expense_no_selection(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.remove_button.invoke()
    assert app.budget_manager.get_current_budget() == 0
    assert app.budget_manager.get_expenses() == []

def test_add_budget(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.budget_entry.insert(0, "100")
    app.add_budget_button.invoke()
    assert app.budget_manager.get_current_budget() == 100

def test_add_budget_invalid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.budget_entry.insert(0, "abc")
    app.add_budget_button.invoke()
    assert app.budget_manager.get_current_budget() == 0

def test_view_monthly_info(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.view_button.invoke()
    assert messagebox.showinfo.called

def test_filter_expenses(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.filter_entry.insert(0, "Test Category")
    app.filter_button.invoke()
    assert app.expense_listbox.get(0) == "Test Category, Test Description, 100"

def test_filter_expenses_no_category(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.filter_button.invoke()
    assert app.expense_listbox.get(0) == ""

def test_update_expense_list(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.update_expense_list()
    assert app.expense_listbox.get(0) == "Test Category, Test Description, 100"

def test_update_budget_label(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager = mock_budget_manager
    app.update_budget_label()
    assert app.budget_label.cget("text") == "Current Budget: $0.00"
```