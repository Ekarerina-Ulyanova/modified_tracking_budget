import tkinter as tk
from tkinter import messagebox
from modified_tracking_budget.budget_manager import BudgetManager

class BudgetApp:
    """
    Represents a budget management application that enables users to efficiently track expenses, manage budgets, and interact with a database.

            Methods:
                - __init__: Initializes the BudgetApp with the given root window, sets the title to "Budget Manager", creates a BudgetManager instance, creates widgets, and updates the expense list.
                - create_widgets: Creates and initializes various widgets for managing budget and expenses in the GUI application.
                - add_expense: Adds an expense to the budget manager based on user input from the GUI.
                - remove_expense: Removes the selected expense from the budget manager, updates the budget amount, and refreshes the expense list displayed in the GUI.
                - add_budget: Adds a new budget amount to the budget manager and updates the budget label in the GUI.
                - view_monthly_info: Displays the monthly information retrieved from the budget manager in a message box.
                - update_expense_list: Updates the expense list displayed in the GUI by clearing the current list and inserting all expenses from the budget manager.
                - update_budget_label: Updates the budget label in the GUI with the current budget amount fetched from the database.

            Attributes:
                - root: The root window for the BudgetApp.
                - budget_manager: Instance of BudgetManager for managing budget and expenses.
    """
    def __init__(self, root):
        """
        Initializes the BudgetApp with the given root window, sets the title to "Budget Manager", creates a BudgetManager instance, creates various widgets for managing budget and expenses in the GUI application, and updates the expense list displayed in the GUI by fetching expenses from the budget manager and adding them to the listbox for display.
        """
        self.root = root
        self.root.title("Budget Manager")
        
        self.budget_manager = BudgetManager()

        self.create_widgets()
        self.update_expense_list()

    def create_widgets(self):
        """
        Creates and initializes various widgets for managing budget and expenses in the GUI application. Widgets include a label for displaying the current budget, entry fields for budget input and expense details, buttons for adding budget and expenses, a listbox for displaying expenses, and buttons for removing expenses and viewing monthly information.
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
        Adds an expense to the budget manager based on user input from the GUI. Retrieves the amount, category, and description of the expense from the respective GUI input fields. If the entered amount is within the current budget limit, deducts the amount from the budget, updates the budget label in the GUI, adds the expense to the budget manager, updates the expense list in the GUI, and displays a success message. If the entered amount exceeds the remaining budget, displays an error message. Handles ValueError by prompting the user to enter a valid number.
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
        Removes the selected expense from the budget manager, updates the budget amount by adding back the expense amount, refreshes the expense list displayed in the GUI, and provides appropriate user feedback through message boxes. If no expense is selected, a warning message is displayed prompting the user to select an expense for removal.
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
        Adds a new budget amount to the budget manager by retrieving the input from the GUI entry field. Updates the budget label in the GUI to display the current budget amount fetched from the database. Displays a success message upon successful update and handles errors for invalid input.
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
        Displays the monthly information retrieved from the budget manager in a message box. Retrieves the monthly information from the budget manager and shows it in a message box using the `showinfo` method from the `messagebox` module.
        """
        info = self.budget_manager.view_monthly_info()
        messagebox.showinfo("Monthly Info", info)

    def update_expense_list(self):
        """
        Updates the expense list displayed in the GUI by clearing the current list and inserting all expenses retrieved from the budget manager. The expenses are fetched from the database and added to the GUI listbox for display.
        """
        self.expense_listbox.delete(0, tk.END)
        for expense in self.budget_manager.get_expenses():
            self.expense_listbox.insert(tk.END, expense)

    def update_budget_label(self):
        """
        Updates the budget label in the GUI with the current budget amount fetched from the database. Fetches the current budget amount using the `get_current_budget` method from the `budget_manager` attribute of the BudgetApp instance. Updates the text of the `budget_label` widget in the GUI to display the current budget amount formatted as a currency value.
        """
        budget = self.budget_manager.get_current_budget()
        self.budget_label.config(text=f"Current Budget: ${budget:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
