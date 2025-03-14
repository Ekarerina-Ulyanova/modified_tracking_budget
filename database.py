import sqlite3

class Database:
    """
Database class for managing expenses and budget."""
    def __init__(self):
        """
Initializes the database connection and creates necessary tables.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
        self.connection = sqlite3.connect('budget.db')
        self.cursor = self.connection.cursor()  # Здесь нужно использовать cursor()
        self.create_tables()

    def create_tables(self):
        """
Creates the expenses and budget tables if they don't exist.

    Initializes the budget table with a default amount of 0 if it is empty.

    Args:
        self: The database connection object.

    Returns:
        None
    """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY,
                amount REAL
            )
        ''')
        
        # Инициализация бюджета, если он не существует
        self.cursor.execute('SELECT COUNT(*) FROM budget')
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute('INSERT INTO budget (id, amount) VALUES (1, 0)')
            self.connection.commit()

    def add_expense(self, amount, category, description):
        """
Adds a new expense to the expenses table.

    Args:
        amount: The amount of the expense.
        category: The category of the expense.
        description: A brief description of the expense.

    Returns:
        None
    """
        self.cursor.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)', 
                            (amount, category, description))
        self.connection.commit()

    def remove_expense(self, expense_id):
        """
Removes an expense from the database.

    Args:
        expense_id: The ID of the expense to be removed.

    Returns:
        None
    """
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.connection.commit()

    def add_budget(self, amount):
        """
Adds the given amount to the current budget.

    Args:
        amount: The amount to add to the budget.

    Returns:
        None
    """
        current_budget = self.get_current_budget()
        new_budget = current_budget + amount
        self.cursor.execute('UPDATE budget SET amount = ? WHERE id = 1', (new_budget,))
        self.connection.commit()

    def get_current_budget(self):
        """
Retrieves the current budget amount from the database.

    Args:
        self: The instance of the class.

    Returns:
        int: The current budget amount.
    """
        self.cursor.execute('SELECT amount FROM budget WHERE id = 1')
        return self.cursor.fetchone()[0]

    def get_expenses(self):
        """
Retrieves all expenses from the database.

    Args:
        self: The instance of the class.

    Returns:
        list: A list of tuples, where each tuple represents an expense 
              with (expense_id, user_id, amount, description).  
              Returns an empty list if no expenses are found.
    """
        self.cursor.execute('SELECT * FROM expenses')
        return [(row[0], row[1], row[2], row[3]) for row in self.cursor.fetchall()]

    def view_monthly_info(self):
        """
Retrieves and displays monthly expense information.

    Args:
        self: The instance of the class.

    Returns:
        str: A string containing a summary of total expenses and a list of individual expenses with their categories.  If no expenses are found, returns a message indicating that.
    """
        expenses = self.get_expenses()
        total_expenses = sum(exp[1] for exp in expenses)
        
        info = f"Total Expenses: ${total_expenses:.2f}\n"
        info += "\n".join([f"{exp[1]} - {exp[2]}: {exp[3]}" for exp in expenses])
        
        return info

    def clear(self):
        """
Removes all data from the database tables.

    Args:
        self: The Database instance.

    Returns:
        None
    """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f"DELETE FROM {table[0]};")
            self.cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table[0]}';")
        self.connection.commit()

    def close(self):
        """
Closes the connection.

  Args:
    self: The instance of the class.

  Returns:
    None
  """
        self.connection.close()
