```python
import pytest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import MagicMock
from main import BudgetApp, BudgetManager

@pytest.fixture
def mock_budget_manager():
    return MagicMock(spec=BudgetManager)

@pytest.fixture
def mock_root():
    return MagicMock(spec=tk.Tk)

def test_budget_app_init(mock_root):
    app = BudgetApp(mock_root)
    assert app.root == mock_root
    assert isinstance(app.budget_manager, BudgetManager)

def test_create_widgets(mock_root):
    app = BudgetApp(mock_root)
    assert app.budget_label
    assert app.budget_entry
    assert app.add_budget_button
    assert app.amount_entry
    assert app.category_entry
    assert app.description_entry
    assert app.add_button
    assert app.expense_listbox
    assert app.remove_button
    assert app.view_button

def test_add_expense_valid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.add_budget = MagicMock()
    app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    app.amount_entry.insert(0, "50")
    app.category_entry.insert(0, "Test Category")
    app.description_entry.insert(0, "Test Description")
    app.add_button.config(command=app.add_expense)
    app.add_button.invoke()
    app.budget_manager.add_budget.assert_called_once_with(-50.0)
    app.budget_manager.add_expense.assert_called_once_with(50.0, "Test Category", "Test Description")

def test_add_expense_invalid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.add_budget = MagicMock()
    app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    app.amount_entry.insert(0, "150")
    app.category_entry.insert(0, "Test Category")
    app.description_entry.insert(0, "Test Description")
    app.add_button.config(command=app.add_expense)
    app.add_button.invoke()
    messagebox.showwarning.assert_called_once_with("Error", "Transaction amount exceeds remaining budget.")

def test_add_expense_invalid_input(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.add_budget = MagicMock()
    app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    app.amount_entry.insert(0, "abc")
    app.category_entry.insert(0, "Test Category")
    app.description_entry.insert(0, "Test Description")
    app.add_button.config(command=app.add_expense)
    app.add_button.invoke()
    messagebox.showerror.assert_called_once_with("Error", "Please enter a valid number.")

def test_remove_expense_valid_selection(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.get_expense_amount = MagicMock(return_value=50.0)
    app.expense_listbox.insert(0, "Test Expense")
    app.remove_button.config(command=app.remove_expense)
    app.remove_button.invoke()
    app.budget_manager.add_budget.assert_called_once_with(50.0)
    app.budget_manager.remove_expense.assert_called_once_with(0)

def test_remove_expense_invalid_selection(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.remove_button.config(command=app.remove_expense)
    app.remove_button.invoke()
    messagebox.showwarning.assert_called_once_with("Warning", "Select an expense to remove.")

def test_add_budget_valid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.add_budget = MagicMock()
    app.budget_entry.insert(0, "100")
    app.add_budget_button.config(command=app.add_budget)
    app.add_budget_button.invoke()
    app.budget_manager.add_budget.assert_called_once_with(100.0)

def test_add_budget_invalid_amount(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.add_budget = MagicMock()
    app.budget_entry.insert(0, "abc")
    app.add_budget_button.config(command=app.add_budget)
    app.add_budget_button.invoke()
    messagebox.showerror.assert_called_once_with("Error", "Please enter a valid amount.")
    app.budget_entry.delete.assert_called_once_with(0, tk.END)

def test_view_monthly_info(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.view_monthly_info = MagicMock(return_value="Test Info")
    app.view_button.config(command=app.view_monthly_info)
    app.view_button.invoke()
    messagebox.showinfo.assert_called_once_with("Monthly Info", "Test Info")

def test_update_expense_list(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.get_expenses = MagicMock(return_value=["Test Expense 1", "Test Expense 2"])
    app.update_expense_list()
    assert app.expense_listbox.get(0, tk.END) == ["Test Expense 1", "Test Expense 2"]

def test_update_budget_label(mock_budget_manager, mock_root):
    app = BudgetApp(mock_root)
    app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    app.update_budget_label()
    assert app.budget_label.cget("text") == "Current Budget: $100.00"
```