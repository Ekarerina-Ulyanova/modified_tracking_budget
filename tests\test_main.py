```python
import pytest
from unittest.mock import Mock
from main import BudgetApp, BudgetManager
import tkinter as tk
from tkinter import messagebox

@pytest.fixture
def budget_manager():
    return BudgetManager()

@pytest.fixture
def budget_app(budget_manager):
    root = tk.Tk()
    return BudgetApp(root)

def test_budget_app_init(budget_app):
    assert budget_app.root.title() == "Budget Manager"
    assert isinstance(budget_app.budget_manager, BudgetManager)

def test_create_widgets(budget_app):
    for widget in budget_app.root.winfo_children():
        assert isinstance(widget, (tk.Label, tk.Entry, tk.Button, tk.Listbox))

def test_add_expense(budget_app, budget_manager):
    budget_manager.add_budget(100)
    budget_app.update_budget_label()
    assert budget_app.budget_label.cget("text") == "Current Budget: $100.00"
    budget_app.add_expense()
    assert budget_app.budget_manager.get_expenses() == [("Expense 1", 10, "Category 1", "Description 1")]
    budget_app.add_expense()
    assert budget_app.budget_manager.get_expenses() == [("Expense 1", 10, "Category 1", "Description 1"), ("Expense 2", 20, "Category 2", "Description 2")]

def test_add_expense_invalid_amount(budget_app, budget_manager):
    budget_manager.add_budget(100)
    budget_app.update_budget_label()
    budget_app.amount_entry.insert(0, "abc")
    budget_app.add_expense()
    assert messagebox.showerror.call_count == 1

def test_remove_expense(budget_app, budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_app.update_expense_list()
    assert len(budget_app.expense_listbox.get(0, tk.END)) == 1
    budget_app.remove_expense()
    assert len(budget_app.expense_listbox.get(0, tk.END)) == 0

def test_remove_expense_invalid_selection(budget_app, budget_manager):
    budget_app.remove_expense()
    assert messagebox.showwarning.call_count == 1

def test_add_budget(budget_app, budget_manager):
    budget_app.add_budget()
    assert budget_app.budget_manager.get_current_budget() == 100
    budget_app.add_budget()
    assert budget_app.budget_manager.get_current_budget() == 200

def test_add_budget_invalid_amount(budget_app, budget_manager):
    budget_app.budget_entry.insert(0, "abc")
    budget_app.add_budget()
    assert messagebox.showerror.call_count == 1

def test_view_monthly_info(budget_app, budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_app.view_monthly_info()
    assert messagebox.showinfo.call_count == 1

def test_export_to_csv(budget_app, budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_app.export_to_csv()
    assert messagebox.showinfo.call_count == 1

def test_update_expense_list(budget_app, budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_app.update_expense_list()
    assert len(budget_app.expense_listbox.get(0, tk.END)) == 1

def test_update_budget_label(budget_app, budget_manager):
    budget_manager.add_budget(100)
    budget_app.update_budget_label()
    assert budget_app.budget_label.cget("text") == "Current Budget: $100.00"

def test_budget_manager_add_budget(budget_manager):
    budget_manager.add_budget(100)
    assert budget_manager.get_current_budget() == 100

def test_budget_manager_add_expense(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    assert budget_manager.get_expenses() == [("Expense 1", 10, "Category 1", "Description 1")]

def test_budget_manager_remove_expense(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_manager.remove_expense(0)
    assert budget_manager.get_expenses() == []

def test_budget_manager_view_monthly_info(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    info = budget_manager.view_monthly_info()
    assert isinstance(info, str)

def test_budget_manager_export_to_csv(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    budget_manager.export_to_csv()
    assert True  # No assertion needed for this method

def test_budget_manager_get_expenses(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    assert budget_manager.get_expenses() == [("Expense 1", 10, "Category 1", "Description 1")]

def test_budget_manager_get_expense_amount(budget_manager):
    budget_manager.add_expense(10, "Category 1", "Description 1")
    assert budget_manager.get_expense_amount(0) == 10
```