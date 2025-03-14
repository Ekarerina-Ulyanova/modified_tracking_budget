import pytest
from main import BudgetApp
import tkinter as tk
from tkinter import messagebox

def mock_showinfo(title, message):
    """
Displays a simple information dialog.

    Args:
        title: The title of the dialog box.
        message: The message to display in the dialog box.

    Returns:
        None
    """
    pass
def mock_showwarning(title, message):
    """
Displays a warning message.

    Args:
        title: The title of the warning dialog.
        message: The text content of the warning message.

    Returns:
        None
    """
    pass
def mock_showerror(title, message):
    """
Displays an error message.

    Args:
        title: The title of the error dialog.
        message: The error message to display.

    Returns:
        None
    """
    pass

@pytest.fixture
def app():
    """
Runs the budget application and yields the main application instance.

    This function initializes the Tkinter root window, creates a BudgetApp 
    instance, runs the application event loop (via yield), then cleans up 
    by clearing data and destroying the root window.

    Args:
        None

    Returns:
        None
    """
    root = tk.Tk()
    app = BudgetApp(root)
    yield app
    app.budget_manager.clear_data()
    root.destroy()

@pytest.fixture(autouse=True)
def override_messagebox():
    """
Overrides the messagebox functions with mock versions for testing.

    This fixture replaces `showinfo`, `showwarning`, and `showerror` from the 
    `tkinter.messagebox` module with mock functions, allowing tests to avoid 
    displaying actual message boxes.  The original functions are restored after 
    the test completes.

    Args:
        None

    Returns:
        None
    """
    original_showinfo = messagebox.showinfo
    original_showwarning = messagebox.showwarning
    original_showerror = messagebox.showerror

    messagebox.showinfo = mock_showinfo
    messagebox.showwarning = mock_showwarning
    messagebox.showerror = mock_showerror

    yield

    messagebox.showinfo = original_showinfo
    messagebox.showwarning = original_showwarning
    messagebox.showerror = original_showerror

def test_add_budget(app):
    """
Tests the add_budget functionality by adding two budget entries and asserting the total.

    Args:
        app: The application instance to test with.

    Returns:
        None
    """
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.budget_entry.insert(0, "500")
    app.add_budget()
    assert app.budget_manager.get_current_budget() == 1500.0

def test_add_expense(app):
    """
Tests the add expense functionality.

    Args:
        app: The application instance to test with.

    Returns:
        None
    """
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    assert app.budget_manager.get_current_budget() == 800.0
    assert len(app.budget_manager.get_expenses()) == 1

def test_expense_more_than_in_budget(app):
    """
Tests adding an expense that exceeds the budget."""
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "1200")
    app.category_entry.insert(0, "Car")
    app.description_entry.insert(0, "Rent for 3 days")
    app.add_expense()
    assert app.budget_manager.get_current_budget() == 1000.0
    assert len(app.budget_manager.get_expenses()) == 0

def test_remove_expense(app):
    """
Tests the remove expense functionality.

    Args:
        app: The application instance to test with.

    Returns:
        None
    """
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    app.expense_listbox.selection_set(0)
    app.remove_expense()
    assert app.budget_manager.get_current_budget() == 1000.0
    assert len(app.budget_manager.get_expenses()) == 0

def test_view_monthly_info(app):
    """
Tests the view_monthly_info functionality.

    This test case adds a budget and two expenses, then asserts that 
    the monthly info string contains the correct total expenses.

    Args:
        app: The application instance to use for testing.

    Returns:
        None
    """
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.amount_entry.insert(0, "200")
    app.category_entry.insert(0, "Food")
    app.description_entry.insert(0, "Groceries")
    app.add_expense()
    app.amount_entry.insert(0, "10")
    app.category_entry.insert(0, "Entertainment")
    app.description_entry.insert(0, "Theater")
    app.add_expense()
    info = app.budget_manager.view_monthly_info()
    assert "Total Expenses: $210.00" in info

if __name__ == "__main__":
    pytest.main()
