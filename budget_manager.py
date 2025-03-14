from database import Database

class BudgetManager:
    """
Manages budget and expenses using a database connection."""
    def __init__(self):
        """
Initializes the class with a Database object.

    Args:
        self: The instance of the class.

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
    description: A brief description of the expense.

  Returns:
    None
  """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        """
Removes an expense from the database.

    Args:
        index: The index of the expense to be removed in the list of expenses.

    Returns:
        None
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
    The expense amount as a number.
  """
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount):
        """
Adds an amount to the budget.

  Args:
    amount: The amount to add to the budget.

  Returns:
    None
  """
        return self.db.add_budget(amount)

    def get_current_budget(self):
        """
Retrieves the current budget.

  Args:
    self: The instance of the class.

  Returns:
    The current budget value.
  """
        return self.db.get_current_budget()

    def get_expenses(self):
        """
Retrieves a list of formatted expense strings.

  Args:
    self: The instance of the class containing the database connection.

  Returns:
    list[str]: A list of strings, where each string represents an expense 
               in the format "$amount - category: description". Returns an empty
               list if there are no expenses.
  """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self):
        """
Retrieves and returns monthly information from the database.

  Args:
    self: The instance of the class.

  Returns:
    None: Returns the result of calling `self.db.view_monthly_info()`.
  """
        return self.db.view_monthly_info()

    def clear_data(self):
        """
Clears all data from the database.

  Args:
    self: The instance of the class.

  Returns:
    None
  """
        self.db.clear()

    def close(self):
        """
Closes the database connection.

  Args:
    self: The instance of the class.

  Returns:
    None
  """
        return self.db.close()
