import pytest
from modified_tracking_budget.__main__ import BudgetApp
import tkinter as tk
from tkinter import messagebox

def mock_showinfo(title, message):
    """
    Mock the showinfo function to display a message dialog with a specified title and message. This method is used for testing purposes to simulate the behavior of the showinfo function without actually displaying a dialog to the user.
    """
    pass
def mock_showwarning(title, message):
    """
    Mock the showwarning function by capturing the title and message parameters. This function is used to simulate the behavior of the showwarning function by accepting and storing the title and message parameters that would typically be displayed in a warning message dialog.
    """
    pass
def mock_showerror(title, message):
    """
    Displays a mock error message dialog with the given title and message. This method is used to simulate showing an error message dialog without actually displaying it to the user. It takes the title of the error message dialog and the content message to be displayed as parameters.
    """
    pass

@pytest.fixture
def app():
    """
    Creates a BudgetApp instance, yields it, clears the data in the budget manager, and destroys the root Tk instance. This method initializes the BudgetApp instance, yields it for further processing, clears all data stored in the budget manager's database, and then destroys the root Tk instance to clean up resources.
    """
    root = tk.Tk()
    app = BudgetApp(root)
    yield app
    app.budget_manager.clear_data()
    root.destroy()

@pytest.fixture(autouse=True)
def override_messagebox():
    """
    Override the default behavior of messagebox methods temporarily for testing purposes.

    This method temporarily replaces the default showinfo, showwarning, and showerror methods of the messagebox module with mock implementations during testing using pytest.

    Yields control back to the caller to allow the testing code to run with the overridden messagebox methods.

    After the testing code completes, the original messagebox methods are restored.
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
    Performs a test to add budget entries to the application and verify the current budget amount by inserting two budget entries of $1000 and $500 respectively, then calling the `add_budget` method for each entry. Finally, it asserts that the current budget amount retrieved from the `budget_manager` object is equal to $1500.0.
    """
    app.budget_entry.insert(0, "1000")
    app.add_budget()
    app.budget_entry.insert(0, "500")
    app.add_budget()
    assert app.budget_manager.get_current_budget() == 1500.0

def test_add_expense(app):
    """
    Performs a test scenario for adding an expense in the application by simulating the addition of an expense with specific details. Verifies that the budget is updated correctly and that the expense is recorded in the application.

    Args:
        app: The application instance to test.

    The method first sets an initial budget amount in the application, then adds a new expense with a specified amount, category, and description. Finally, it asserts that the current budget amount is updated correctly and that the number of recorded expenses is incremented by one.
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
    Test if the expense is more than the budget in the application by simulating adding a budget and an expense. This method ensures that the current budget amount is correctly set to 1000.0 and that no expenses are added to the budget manager.
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
    Performs a test to validate the functionality of removing an expense from the budget manager within the provided 'app' instance.

    Args:
        app: The application instance containing the budget manager and necessary UI elements.

    The method simulates the process of adding an expense to the budget manager, selecting and removing that expense, and then asserts that the current budget is correct and the expenses list is empty after removal.
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
    Test the functionality of viewing monthly information in the budget app by simulating the addition of expenses and checking the total expenses displayed. This test function interacts with the BudgetApp instance provided to add expenses and then retrieves the monthly information using the `view_monthly_info` method from the budget manager. It asserts that the total expenses are correctly displayed in the retrieved information.
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
