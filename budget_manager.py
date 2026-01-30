```python
from database import Database

class BudgetManager:
    """Custom class for managing budgets and expenses"""

    def __init__(self):
        self.db = Database()

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Add a new expense to the database"""
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index: int) -> bool:
        """Remove an expense from the database by index"""
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_id = expenses[index][0]
            return self.db.remove_expense(expense_id)
        return False

    def get_expense_amount(self, index: int) -> float:
        """Get the amount of an expense by index"""
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_amount = expenses[index][1]
            return expense_amount
        return 0.0

    def add_budget(self, amount: float) -> None:
        """Add a new budget to the database"""
        return self.db.add_budget(amount)

    def get_current_budget(self) -> float:
        """Get the current budget from the database"""
        return self.db.get_current_budget()

    def get_expenses(self) -> list[str]:
        """Get a list of expenses in a human-readable format"""
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self) -> dict:
        """Get monthly information from the database"""
        return self.db.view_monthly_info()

    def clear_data(self) -> None:
        """Clear all data from the database"""
        self.db.clear()

    def close(self) -> None:
        """Close the database connection"""
        return self.db.close()
```