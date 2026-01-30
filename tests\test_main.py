```python
import pytest
import tkinter as tk
from unittest.mock import MagicMock
from budget_manager import BudgetManager

@pytest.fixture
def mock_budget_manager():
    return MagicMock(spec=BudgetManager)

@pytest.fixture
def mock_root():
    return MagicMock(spec=tk.Tk)

def test_budget_app_init(mock_root):
    budget_app = BudgetApp(mock_root)
    assert budget_app.root == mock_root
    assert budget_app.budget_manager == BudgetManager()

def test_create_widgets(mock_root):
    budget_app = BudgetApp(mock_root)
    assert budget_app.budget_label.winfo_exists()
    assert budget_app.budget_entry.winfo_exists()
    assert budget_app.add_budget_button.winfo_exists()
    assert budget_app.amount_entry.winfo_exists()
    assert budget_app.category_entry.winfo_exists()
    assert budget_app.description_entry.winfo_exists()
    assert budget_app.add_button.winfo_exists()
    assert budget_app.expense_listbox.winfo_exists()
    assert budget_app.remove_button.winfo_exists()
    assert budget_app.view_button.winfo_exists()
    assert budget_app.filter_button.winfo_exists()
    assert budget_app.filter_label.winfo_exists()
    assert budget_app.filter_entry.winfo_exists()

def test_add_expense(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.add_budget = MagicMock()
    budget_app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    budget_app.amount_entry.insert(0, "50")
    budget_app.category_entry.insert(0, "Food")
    budget_app.description_entry.insert(0, "Groceries")
    budget_app.add_expense()
    budget_app.budget_manager.add_budget.assert_called_once_with(50)
    budget_app.budget_manager.add_expense.assert_called_once_with(50, "Food", "Groceries")

def test_add_expense_invalid_amount(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.add_budget = MagicMock()
    budget_app.budget_manager.get_current_budget = MagicMock(return_value=100.0)
    budget_app.amount_entry.insert(0, "150")
    budget_app.category_entry.insert(0, "Food")
    budget_app.description_entry.insert(0, "Groceries")
    budget_app.add_expense()
    budget_app.budget_manager.add_budget.assert_not_called()
    budget_app.budget_manager.add_expense.assert_not_called()

def test_remove_expense(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.get_expense_amount = MagicMock(return_value=50)
    budget_app.budget_manager.add_budget = MagicMock()
    budget_app.remove_expense()
    budget_app.budget_manager.add_budget.assert_called_once_with(50)

def test_remove_expense_no_selection(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.remove_expense()
    budget_app.budget_manager.add_budget.assert_not_called()

def test_view_monthly_info(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.view_monthly_info = MagicMock(return_value="Monthly info")
    budget_app.view_monthly_info()
    budget_app.budget_manager.view_monthly_info.assert_called_once()

def test_filter_expenses(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.filter_expenses()
    budget_app.budget_manager.get_expenses.assert_called_once()

def test_filter_expenses_by_category(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.filter_expenses_by_category("Food")
    budget_app.budget_manager.get_expenses.assert_called_once()

def test_update_expense_list(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.update_expense_list()
    budget_app.budget_manager.get_expenses.assert_called_once()

def test_update_budget_label(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.update_budget_label()
    budget_app.budget_manager.get_current_budget.assert_called_once()

def test_add_budget(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.add_budget = MagicMock()
    budget_app.add_budget()
    budget_app.budget_manager.add_budget.assert_called_once_with(0)

def test_add_budget_invalid_amount(mock_budget_manager, mock_root):
    budget_app = BudgetApp(mock_root)
    budget_app.budget_manager.add_budget = MagicMock()
    budget_app.budget_entry.insert(0, "abc")
    budget_app.add_budget()
    budget_app.budget_manager.add_budget.assert_not_called()
```