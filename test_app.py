import pytest
from main import BudgetApp
import tkinter as tk
from tkinter import messagebox

def mock_showinfo(title, message):
    """
Displays an informational message with a given title.

    This function is a mock implementation that simulates the display
    of an informational message box with a specified title and message.
    It does not perform any actual display operation.

    Args:
        title (str): The title of the informational message box.
        message (str): The message content to be displayed.

    Returns:
        None
    """
    pass
def mock_showwarning(title, message):
    """
Displays a warning message with a specified title.

    This function is a mock implementation that simulates the behavior of 
    showing a warning message. It takes a title and a message as input 
    parameters but does not perform any actual operation.

    Args:
        title (str): The title of the warning message.
        message (str): The content of the warning message.

    Returns:
        None: This function does not return any value.
    """
    pass
def mock_showerror(title, message):
    """
Displays an error message with a specified title.

    This function is a placeholder for displaying an error dialog. 
    It takes a title and a message as input parameters but does not 
    perform any action.

    Args:
        title (str): The title of the error dialog.
        message (str): The error message to be displayed.

    Returns:
        None
    """
    pass

@pytest.fixture
def app():
    root = tk.Tk()
    app = BudgetApp(root)
    yield app
    app.budget_manager.clear_data()
    root.destroy()

@pytest.fixture(autouse=True)
def override_messagebox():
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
Tests the addition of budget entries in the application.

    This method simulates the process of adding budget entries to the 
    application's budget manager. It inserts two budget amounts into 
    the budget entry field and verifies that the total budget is 
    correctly updated.

    Args:
        app (YourAppType): An instance of the application that contains 
                           the budget entry and budget manager.

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
Tests the functionality of adding an expense to the budget.

    This method simulates the process of adding an expense to the budget
    by inserting values into the application's entry fields and invoking
    the appropriate methods to add the budget and expense. It then asserts
    that the current budget is updated correctly and that the expense list
    contains the expected number of expenses.

    Args:
        app: An instance of the application that contains the budget manager
             and entry fields for budget and expenses.

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
Tests the behavior of adding an expense that exceeds the budget.

    This method simulates the process of adding a budget and then attempting
    to add an expense that is greater than the allocated budget. It asserts
    that the current budget remains unchanged and that no expenses are recorded.

    Args:
        app: An instance of the application under test, which provides access
            to the budget and expense management functionalities.

    Returns:
        None
    """
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
Test the removal of an expense from the budget.

    This method simulates adding a budget and an expense, then removes the 
    expense and verifies that the budget remains unchanged and that there 
    are no expenses left.

    Args:
        app: An instance of the application containing the budget and expense 
             management functionalities. It is expected to have methods for 
             adding budgets and expenses, as well as removing expenses.

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
Tests the monthly budget information view.

    This method simulates adding a budget and multiple expenses to the 
    application and then verifies that the monthly information reflects 
    the correct total expenses.

    Args:
        app: An instance of the application that contains methods for 
             managing budget entries and expenses.

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
