from modified_tracking_budget.database import Database

class BudgetManager:
    """
    Custom class
    """
    def __init__(self):
        """
        Initializes a new instance of the class by creating an instance of the Database class and assigning it to the 'db' class field.
        """
        self.db = Database()

    def add_expense(self, amount, category, description):
        """
        Adds a new expense to the database by calling the corresponding method in the database interface with the provided amount, category, and description.
        """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        """
        Remove an expense from the database based on the provided index.

        Args:
        - index: The index of the expense to be removed from the database.

        The method retrieves the list of expenses from the database, identifies the expense ID using the provided index, and then removes the expense from the database using the identified expense ID.
        """
        expenses = self.db.get_expenses()
        expense_id = expenses[index][0]
        return self.db.remove_expense(expense_id)

    def get_expense_amount(self, index):
        """
        Get the amount of a specific expense based on the provided index.

        Args:
        - index: The index of the expense in the list.

        The method retrieves the list of expenses from the database, accesses the expense amount at the specified index, and returns it.
        """
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount):
        """
        Adds a budget amount to the database by invoking the `add_budget` method of the database interface.
        """
        return self.db.add_budget(amount)

    def get_current_budget(self):
        """
        Get the current budget from the database.

        Retrieves the current budget from the database by calling the `get_current_budget` method of the `db` object associated with the BudgetManager instance.
        """
        return self.db.get_current_budget()

    def get_expenses(self):
        """
        Retrieves a list of formatted expenses from the database.

        Args:
            self: Instance of the BudgetManager class.

        Returns:
            List of strings representing expenses in the format "$<amount> - <category>: <description>".
        """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self):
        """
        Retrieves and returns monthly information from the database by calling the corresponding method in the database interface.
        """
        return self.db.view_monthly_info()

    def clear_data(self):
        """
        Clears all data stored in the database by invoking the clear method of the database object.
        """
        self.db.clear()

    def close(self):
        """
        Closes the database connection by invoking the close method on the database object.
        """
        return self.db.close()

#Test update
