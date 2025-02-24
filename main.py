import tkinter as tk
from tkinter import messagebox
from budget_manager import BudgetManager

class BudgetApp:
    """
    A budget management application that allows users to track their expenses 
    and manage their budget effectively.

    This application provides a user-friendly interface for adding and removing 
    expenses, setting a budget, and viewing monthly budget information.

    Methods:
        __init__: Initializes the Budget Manager application.
        create_widgets: Create and configure the user interface widgets for the budget manager.
        add_expense: Add an expense to the budget.
        remove_expense: Remove the selected expense from the expense list.
        add_budget: Adds a budget amount entered by the user.
        view_monthly_info: Displays the monthly budget information in a message box.
        update_expense_list: Updates the displayed list of expenses in the expense listbox.
        update_budget_label: Update the budget label with the current budget amount.

    Attributes:
        root (Tk): The root window of the application.
        budget_manager (BudgetManager): An instance of the budget manager handling the budget logic.
    """
    def __init__(self, root):
        """
Initializes the Budget Manager application.

    This method sets up the main window for the Budget Manager application,
    initializes the budget manager instance, and creates the necessary
    widgets for the user interface.

    Args:
        root (Tk): The root window of the application, typically an instance
            of Tkinter's Tk class.

    Returns:
        None
    """
        self.root = root
        self.root.title("Budget Manager")
        
        self.budget_manager = BudgetManager()

        self.create_widgets()
        self.update_expense_list()

    def create_widgets(self):
        """
Create and configure the user interface widgets for the budget manager.

    This method initializes various UI components such as labels, entry fields, 
    and buttons for managing the budget and expenses. It sets up the layout 
    of the widgets within the main application window.

    Args:
        self: The instance of the class that contains the method.

    Returns:
        None
    """
        self.budget_label = tk.Label(self.root, text= f"Current Budget: ${self.budget_manager.get_current_budget():.2f}")
        self.budget_label.pack()

        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.pack()
        self.budget_entry.insert(0, "")

        self.add_budget_button = tk.Button(self.root, text="Add Budget", command=self.add_budget)
        self.add_budget_button.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        self.amount_entry.insert(0, "")

        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()
        self.category_entry.insert(0, "")

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()
        self.description_entry.insert(0, "")

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expense_listbox = tk.Listbox(self.root)
        self.expense_listbox.pack()

        self.remove_button = tk.Button(self.root, text="Remove Expense", command=self.remove_expense)
        self.remove_button.pack()

        self.view_button = tk.Button(self.root, text="View Monthly Info", command=self.view_monthly_info)
        self.view_button.pack()

    def add_expense(self):
        """
Add an expense to the budget.

    This method retrieves the amount, category, and description of an expense 
    from the respective entry fields, validates the amount against the current 
    budget, and updates the budget and expense list accordingly. If the 
    transaction is successful, a success message is displayed; otherwise, 
    appropriate error messages are shown.

    Raises:
        ValueError: If the amount entered is not a valid number.

    Returns:
        None
    """
        try:
            amount = float(self.amount_entry.get())
            self.amount_entry.delete(0, tk.END)
            category = self.category_entry.get()
            self.category_entry.delete(0, tk.END)
            description = self.description_entry.get()
            self.description_entry.delete(0, tk.END)
            if amount <= self.budget_manager.get_current_budget():
                self.budget_manager.add_budget(-amount)
                self.update_budget_label()
                self.budget_manager.add_expense(amount, category, description)
                self.update_expense_list()
                messagebox.showinfo("Success", "Transaction added!")
            else:
                messagebox.showwarning("Error", "Transaction amount exceeds remaining budget.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def remove_expense(self):
        """
Remove the selected expense from the expense list.

    This method retrieves the currently selected expense from the 
    expense listbox, adds the corresponding amount back to the budget, 
    and updates the budget label. If an expense is successfully removed, 
    a success message is displayed. If no expense is selected, a warning 
    message is shown.

    Args:
        self: The instance of the class that contains the method.

    Returns:
        None: This method does not return any value.
    """
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            amount = self.budget_manager.get_expense_amount(selected_index[0])
            self.budget_manager.add_budget(amount)
            self.update_budget_label()
            self.budget_manager.remove_expense(selected_index[0])
            self.update_expense_list()
            messagebox.showinfo("Success", "Expense removed successfully!")
        else:
            messagebox.showwarning("Warning", "Select an expense to remove.")

    def add_budget(self):
        """
Adds a budget amount entered by the user.

    This method retrieves the budget amount from the user interface, 
    attempts to convert it to a float, and then adds it to the budget 
    manager. If the conversion is successful, it updates the budget 
    label and clears the input field. If the input is invalid, it 
    displays an error message and clears the input field.

    Raises:
        ValueError: If the input cannot be converted to a float.

    Returns:
        None
    """
        try:
            amount = float(self.budget_entry.get())
            self.budget_manager.add_budget(amount)
            self.update_budget_label()
            self.budget_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Budget updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            self.budget_entry.delete(0, tk.END)

    def view_monthly_info(self):
        """
Displays the monthly budget information in a message box.

    This method retrieves the monthly budget information from the 
    budget manager and displays it in a message box for the user.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
        info = self.budget_manager.view_monthly_info()
        messagebox.showinfo("Monthly Info", info)

    def update_expense_list(self):
        """
Updates the displayed list of expenses in the expense listbox.

    This method clears the current items in the expense listbox and populates it
    with the latest expenses retrieved from the budget manager.

    Args:
        self: The instance of the class that contains the expense listbox and budget manager.

    Returns:
        None
    """
        self.expense_listbox.delete(0, tk.END)
        for expense in self.budget_manager.get_expenses():
            self.expense_listbox.insert(tk.END, expense)

    def update_budget_label(self):
        """
Update the budget label with the current budget amount.

    This method retrieves the current budget from the budget manager
    and updates the label to display the current budget in a formatted
    string.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
        budget = self.budget_manager.get_current_budget()
        self.budget_label.config(text=f"Current Budget: ${budget:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
