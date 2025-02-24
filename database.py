import sqlite3

class Database:
    """
    A class to manage a SQLite database for tracking expenses and budget.

    This class provides methods to create tables, add and remove expenses, 
    manage the budget, and retrieve financial information from the database.

    Methods:
        __init__: Initializes a new instance of the class and establishes a database connection.
        create_tables: Creates necessary tables in the database for expenses and budget.
        add_expense: Inserts a new expense record into the database.
        remove_expense: Deletes an expense entry from the database based on its ID.
        add_budget: Updates the current budget by adding a specified amount.
        get_current_budget: Retrieves the current budget amount from the database.
        get_expenses: Fetches all expense records from the database.
        view_monthly_info: Displays the total expenses for the month with a breakdown.
        clear: Clears all data from all tables in the database.
        close: Closes the database connection and releases resources.
    """
    def __init__(self):
        """
Initializes a new instance of the class.

    This method establishes a connection to a SQLite database named 'budget.db'
    and creates a cursor object for executing SQL commands. It also calls the
    method to create necessary tables in the database.

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
Create the necessary tables in the database.

    This method creates two tables: 'expenses' and 'budget'. 
    The 'expenses' table is designed to store expense records with 
    fields for the amount, category, and description. The 'budget' 
    table is intended to hold the budget amount. If the 'budget' 
    table is empty, it initializes it with a default entry.

    Args:
        self: The instance of the class that contains the database connection 
              and cursor for executing SQL commands.

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
Add a new expense record to the database.

    This method inserts a new expense entry into the 'expenses' table with the specified amount, category, and description.
    After executing the insert operation, it commits the changes to the database.

    Args:
        amount (float): The amount of the expense.
        category (str): The category of the expense (e.g., 'Food', 'Transport').
        description (str): A brief description of the expense.

    Returns:
        None
    """
        self.cursor.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)', 
                            (amount, category, description))
        self.connection.commit()

    def remove_expense(self, expense_id):
        """
Removes an expense from the database.

    This method deletes an expense entry from the expenses table in the database
    based on the provided expense ID. It executes a DELETE SQL command and commits
    the changes to the database.

    Args:
        expense_id (int): The unique identifier of the expense to be removed.

    Returns:
        None
    """
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.connection.commit()

    def add_budget(self, amount):
        """
Adds a specified amount to the current budget.

    This method retrieves the current budget, adds the provided amount to it, 
    and updates the budget in the database.

    Args:
        amount (float): The amount to be added to the current budget.

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

    This method executes a SQL query to fetch the current budget amount 
    associated with a specific identifier from the budget table.

    Args:
        self: The instance of the class that this method belongs to.

    Returns:
        None: This method does not return a value. It is intended to 
        retrieve the current budget amount for internal use.
    """
        self.cursor.execute('SELECT amount FROM budget WHERE id = 1')
        return self.cursor.fetchone()[0]

    def get_expenses(self):
        """
Retrieves all expense records from the database.

    This method queries the database for all entries in the expenses table 
    and returns a list of tuples, where each tuple contains the details of 
    an expense record.

    Args:
        self: The instance of the class.

    Returns:
        None: This method does not return any value.
    """
        self.cursor.execute('SELECT * FROM expenses')
        return [(row[0], row[1], row[2], row[3]) for row in self.cursor.fetchall()]

    def view_monthly_info(self):
        """
Display the monthly financial information.

    This method calculates and displays the total expenses for the month,
    along with a detailed breakdown of each expense entry.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
        expenses = self.get_expenses()
        total_expenses = sum(exp[1] for exp in expenses)
        
        info = f"Total Expenses: ${total_expenses:.2f}\n"
        info += "\n".join([f"{exp[1]} - {exp[2]}: {exp[3]}" for exp in expenses])
        
        return info

    def clear(self):
        """
Clears all data from all tables in the database.

    This method retrieves all table names from the database and deletes all records 
    from each table. It also resets the auto-increment sequence for each table to 
    ensure that new entries start from the beginning.

    Args:
        self: The instance of the class that contains the database connection and cursor.

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
Closes the current instance and releases any resources.

    This method performs necessary cleanup operations to ensure that 
    the instance is properly closed and any associated resources are 
    released. It should be called when the instance is no longer needed 
    to prevent resource leaks.

    Args:
        self: The instance of the class that is being closed.

    Returns:
        None
    """
        self.connection.close()
