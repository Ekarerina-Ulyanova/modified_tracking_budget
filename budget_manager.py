from database import Database


class BudgetManager:
    """Custom class"""

    def __init__(self):
        """
        Initializes the BudgetManager with a Database connection.

        Args:
            None

        Returns:
            None
        """
        self.db = Database()

    def add_expense(self, amount, category, description):
        """
        Adds a new expense to the database.

        Args:
            amount: The amount of the expense.
            category: The category of the expense.
            description: A description of the expense.

        Returns:
            The result of adding the expense to the database.
        """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        """
        Removes an expense from the database.

        Args:
            index: The index of the expense to remove from the list of expenses.

        Returns:
            bool: True if the expense was successfully removed, False otherwise.
        """
        expenses = self.db.get_expenses()
        expense_id = expenses[index][0]
        return self.db.remove_expense(expense_id)

    def get_expense_amount(self, index):
        """
        Retrieves the amount of an expense at a given index.

        Args:
            index: The index of the expense to retrieve the amount from.

        Returns:
            float: The amount of the expense at the specified index.

        """
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount):
        """
        Adds a budget to the database.

        Args:
            amount: The amount of the budget to add.

        Returns:
            The result of adding the budget to the database.
        """
        return self.db.add_budget(amount)

    def get_current_budget(self):
        """
        Retrieves the current budget.

        Args:
            None

        Returns:
            The current budget.
        """
        return self.db.get_current_budget()

    def get_expenses(self):
        """
        Retrieves a list of expenses formatted as strings.

        Args:
            self: The instance of the class containing the method.

        Returns:
            list[str]: A list of strings, where each string represents an expense
                       in the format "$amount - category: description".
        """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self):
        """
        Retrieves monthly information from the database.

            Returns:
                A dataset containing monthly information.
        """
        return self.db.view_monthly_info()

    def clear_data(self):
        """
        Clears all data from the database.

        Args:
            None

        Returns:
            None
        """
        self.db.clear()

    def close(self):
        """
        Closes the database connection.

        Args:
            None

        Returns:
            Any: The return value of the underlying database close method.
        """
        return self.db.close()


# Test update
