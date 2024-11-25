from database import Database

class BudgetManager:
    def __init__(self):
        self.db = Database()

    def add_expense(self, amount, category, description):
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        expenses = self.db.get_expenses()
        if index < len(expenses):
            expense_id = expenses[index][0]
            return self.db.remove_expense(expense_id)

    def add_budget(self, amount):
        return self.db.add_budget(amount)

    def get_current_budget(self):
        return self.db.get_current_budget()

    def get_expenses(self):
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def save_data(self):
        return self.db.save_data()

    def view_monthly_info(self):
        return self.db.view_monthly_info()

    def close(self):
        return self.db.close()