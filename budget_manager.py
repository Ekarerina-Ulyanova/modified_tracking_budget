```python
from database import Database

class BudgetManager:
    """Custom class for managing budgets and expenses"""

    def __init__(self):
        self.db = Database()

    def add_expense(self, amount: float, category: str, description: str) -> bool:
        """Add a new expense to the database

        Args:
            amount (float): The amount of the expense
            category (str): The category of the expense
            description (str): A description of the expense

        Returns:
            bool: True if the expense was added successfully, False otherwise
        """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index: int) -> bool:
        """Remove an expense from the database by its index

        Args:
            index (int): The index of the expense to remove

        Returns:
            bool: True if the expense was removed successfully, False otherwise
        """
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_id = expenses[index][0]
            return self.db.remove_expense(expense_id)
        return False

    def get_expense_amount(self, index: int) -> float:
        """Get the amount of an expense by its index

        Args:
            index (int): The index of the expense

        Returns:
            float: The amount of the expense
        """
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_amount = expenses[index][1]
            return expense_amount
        return 0.0

    def add_budget(self, amount: float) -> bool:
        """Add a new budget to the database

        Args:
            amount (float): The amount of the budget

        Returns:
            bool: True if the budget was added successfully, False otherwise
        """
        return self.db.add_budget(amount)

    def get_current_budget(self) -> float:
        """Get the current budget from the database

        Returns:
            float: The current budget
        """
        return self.db.get_current_budget()

    def get_expenses(self) -> list:
        """Get a list of all expenses in the database

        Returns:
            list: A list of strings representing the expenses
        """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self) -> dict:
        """Get a dictionary of monthly information from the database

        Returns:
            dict: A dictionary containing monthly information
        """
        return self.db.view_monthly_info()

    def clear_data(self) -> None:
        """Clear all data from the database"""
        self.db.clear()

    def close(self) -> None:
        """Close the database connection"""
        self.db.close()
```