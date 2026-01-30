from database import Database

class BudgetManager:
    """Custom class"""
    def __init__(self):
        self.db = Database()

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Add a new expense to the database"""
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index: int) -> None:
        """Remove an expense from the database by its index"""
        expenses = self.db.get_expenses()
        expense_id = expenses[index][0]
        return self.db.remove_expense(expense_id)

    def get_expense_amount(self, index: int) -> float:
        """Get the amount of an expense by its index"""
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount: float) -> None:
        """Add a new budget to the database"""
        return self.db.add_budget(amount)

    def get_current_budget(self) -> float:
        """Get the current budget from the database"""
        return self.db.get_current_budget()

    def get_expenses(self) -> list:
        """Get a list of all expenses from the database"""
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self) -> dict:
        """Get a dictionary containing monthly information from the database"""
        return self.db.view_monthly_info()

    def clear_data(self) -> None:
        """Clear all data from the database"""
        self.db.clear()

    def close(self) -> None:
        """Close the database connection"""
        return self.db.close()

    def get_total_expenses(self) -> float:
        """Get the total amount of all expenses from the database"""
        expenses = self.db.get_expenses()
        return sum(exp[1] for exp in expenses)

    def get_average_expense(self) -> float:
        """Get the average amount of all expenses from the database"""
        total_expenses = self.get_total_expenses()
        num_expenses = len(self.db.get_expenses())
        return total_expenses / num_expenses if num_expenses > 0 else 0.0