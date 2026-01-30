```python
import pytest
from unittest.mock import Mock
from main import BudgetApp, BudgetManager

@pytest.fixture
def budget_manager():
    return BudgetManager()

@pytest.fixture
def budget_app(budget_manager):
    root = Mock()
    return BudgetApp(root)

def test_budget_app_init(budget_app):
    assert budget_app.root.title() == "Budget Manager"
    assert isinstance(budget_app.budget_manager, BudgetManager)

def test_create_widgets(budget_app):
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

def test_add_expense(budget_app, budget_manager):
    budget_manager.add_budget = Mock(return_value=None)
    budget_manager.add_expense = Mock(return_value=None)
    budget_app.amount_entry.insert(0, "10.99")
    budget_app.category_entry.insert(0, "Test Category")
    budget_app.description_entry.insert(0, "Test Description")
    budget_app.add_expense()
    budget_manager.add_budget.assert_called_once_with(-10.99)
    budget_manager.add_expense.assert_called_once_with(10.99, "Test Category", "Test Description")

def test_add_expense_invalid_amount(budget_app, budget_manager):
    budget_manager.add_budget = Mock(return_value=None)
    budget_manager.add_expense = Mock(return_value=None)
    budget_app.amount_entry.insert(0, "abc")
    budget_app.add_expense()
    budget_manager.add_budget.assert_not_called()
    budget_manager.add_expense.assert_not_called()

def test_remove_expense(budget_app, budget_manager):
    budget_manager.get_expense_amount = Mock(return_value=10.99)
    budget_manager.add_budget = Mock(return_value=None)
    budget_manager.remove_expense = Mock(return_value=None)
    budget_app.expense_listbox.insert(0, "Test Expense")
    budget_app.remove_expense()
    budget_manager.add_budget.assert_called_once_with(10.99)
    budget_manager.remove_expense.assert_called_once_with(0)

def test_remove_expense_no_selection(budget_app, budget_manager):
    budget_manager.get_expense_amount = Mock(return_value=10.99)
    budget_manager.add_budget = Mock(return_value=None)
    budget_manager.remove_expense = Mock(return_value=None)
    budget_app.remove_expense()
    budget_manager.add_budget.assert_not_called()
    budget_manager.remove_expense.assert_not_called()

def test_add_budget(budget_app, budget_manager):
    budget_manager.add_budget = Mock(return_value=None)
    budget_app.budget_entry.insert(0, "10.99")
    budget_app.add_budget()
    budget_manager.add_budget.assert_called_once_with(10.99)

def test_add_budget_invalid_amount(budget_app, budget_manager):
    budget_manager.add_budget = Mock(return_value=None)
    budget_app.budget_entry.insert(0, "abc")
    budget_app.add_budget()
    budget_manager.add_budget.assert_not_called()

def test_view_monthly_info(budget_app, budget_manager):
    budget_manager.view_monthly_info = Mock(return_value="Test Info")
    budget_app.view_monthly_info()
    budget_manager.view_monthly_info.assert_called_once()

def test_update_expense_list(budget_app, budget_manager):
    budget_manager.get_expenses = Mock(return_value=["Test Expense 1", "Test Expense 2"])
    budget_app.update_expense_list()
    assert budget_app.expense_listbox.get(0, tk.END) == ["Test Expense 1", "Test Expense 2"]

def test_update_budget_label(budget_app, budget_manager):
    budget_manager.get_current_budget = Mock(return_value=10.99)
    budget_app.update_budget_label()
    assert budget_app.budget_label.cget("text") == "Current Budget: $10.99"

def test_save_data(budget_app, budget_manager):
    budget_manager.save_data = Mock(return_value=None)
    budget_app.save_data()
    budget_manager.save_data.assert_called_once()

def test_load_data(budget_app, budget_manager):
    budget_manager.load_data = Mock(return_value=None)
    budget_app.load_data()
    budget_manager.load_data.assert_called_once()
```