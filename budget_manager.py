from database import Database

class BudgetManager:
    """
    A class to manage personal budgeting by tracking expenses and budget amounts.

    This class provides methods to add, remove, and retrieve expenses, as well as 
    manage the overall budget. It interacts with a database to store and retrieve 
    financial data, allowing users to maintain an organized overview of their 
    financial activities.

    Methods:
        __init__: Initializes a new instance of the class.
        add_expense: Adds an expense entry to the database.
        remove_expense: Removes an expense from the database.
        get_expense_amount: Retrieves the amount of an expense at a specified index.
        add_budget: Adds a specified amount to the budget.
        get_current_budget: Retrieves the current budget from the database.
        get_expenses: Retrieves and formats a list of expenses from the database.
        view_monthly_info: Displays monthly information from the database.
        clear_data: Clears all data from the database.
        close: Closes the database connection.

    """
    def __init__(self):
        """
Initializes a new instance of the class.

    This constructor method creates a new instance of the class and initializes
    the database connection by creating an instance of the Database class.

    Args:
        self: The instance of the class being created.

    Returns:
        None
    """
        self.db = Database()

    def add_expense(self, amount, category, description):
        """
Adds an expense entry to the database.

    This method takes the details of an expense and stores it in the database.

    Args:
        amount (float): The amount of the expense.
        category (str): The category under which the expense falls.
        description (str): A brief description of the expense.

    Returns:
        None
    """
        return self.db.add_expense(amount, category, description)

    def remove_expense(self, index):
        """
Remove an expense from the database.

    This method retrieves the list of expenses from the database, identifies 
    the expense at the specified index, and removes it from the database.

    Args:
        index (int): The index of the expense to be removed from the list of expenses.

    Returns:
        None
    """
        expenses = self.db.get_expenses()
        expense_id = expenses[index][0]
        return self.db.remove_expense(expense_id)

    def get_expense_amount(self, index):
        """
Retrieve the amount of an expense at a specified index.

    This method accesses the database to retrieve a list of expenses 
    and returns the amount associated with the expense at the given index.

    Args:
        index (int): The index of the expense in the expenses list.

    Returns:
        float: The amount of the expense at the specified index.
    """
        expenses = self.db.get_expenses()
        expense_amount = expenses[index][1]
        return expense_amount

    def add_budget(self, amount):
        """
Adds a specified amount to the budget.

    This method interacts with the database to add the provided 
    amount to the current budget.

    Args:
        amount (float): The amount of money to be added to the budget.

    Returns:
        None
    """
        return self.db.add_budget(amount)

    def get_current_budget(self):
        """
Retrieves the current budget from the database.

    This method interacts with the database to fetch the current budget information.

    Args:
        self: The instance of the class.

    Returns:
        None: This method does not return any value.
    """
        return self.db.get_current_budget()

    def get_expenses(self):
        """
Retrieve and format a list of expenses from the database.

    This method fetches expenses from the database and formats them into a 
    human-readable string representation, including the amount and description 
    of each expense.

    Args:
        self: The instance of the class.

    Returns:
        None: This method does not return a value; it is intended to be used 
        for side effects (e.g., printing or logging the formatted expenses).
    """
        return [f"${exp[1]:.2f} - {exp[2]}: {exp[3]}" for exp in self.db.get_expenses()]

    def view_monthly_info(self):
        """
Display monthly information from the database.

    This method retrieves and displays the monthly information stored in the database.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
        return self.db.view_monthly_info()

    def clear_data(self):
        """
Clears all data from the database.

    This method invokes the clear method on the database instance,
    effectively removing all stored data.

    Args:
        self: The instance of the class that contains the database.

    Returns:
        None
    """
        self.db.clear()

    def close(self):
        """
Closes the database connection.

    This method terminates the connection to the database, ensuring that 
    all resources are released and any pending transactions are finalized.

    Args:
        self: The instance of the class that contains the database connection.

    Returns:
        None
    """
        return self.db.close()
