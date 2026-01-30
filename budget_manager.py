```python
from database import Database

class BudgetManager:
    """Custom class for managing budgets and expenses"""

    def __init__(self):
        self.db = Database()

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Add a new expense to the database.

        Args:
            amount (float): The amount of the expense.
            category (str): The category of the expense.
            description (str): A description of the expense.
        """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index: int) -> None:
        """Remove an expense from the database by its index.

        Args:
            index (int): The index of the expense to remove.
        """
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_id = expenses[index][0]
            return self.db.remove_expense(expense_id)
        else:
            raise IndexError("Index out of range")

    def get_expense_amount(self, index: int) -> float:
        """Get the amount of an expense by its index.

        Args:
            index (int): The index of the expense.

        Returns:
            float: The amount of the expense.
        """
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_amount = expenses[index][1]
            return expense_amount
        else:
            raise IndexError("Index out of range")

    def add_budget(self, amount: float) -> None:
        """Add a new budget to the database.

        Args:
            amount (float): The amount of the budget.
        """
        return self.db.add_budget(amount)

    def get_current_budget(self) -> float:
        """Get the current budget from the database.

        Returns:
            float: The current budget.
        """
        return self.db.get_current_budget()

    def get_expenses(self) -> list:
        """Get a list of all expenses in the database.

        Returns:
            list: A list of expenses in the format "amount - category: description".
        """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self) -> None:
        """View monthly information from the database.

        This method is not implemented in the database module, so it does nothing.
        """
        pass

    def clear_data(self) -> None:
        """Clear all data from the database.
        """
        self.db.clear()

    def close(self) -> None:
        """Close the database connection.
        """
        return self.db.close()
```