import sqlite3

class Database:
    """
    Manages expenses and budget data within a SQLite database for efficient tracking and management.

            Methods:
            - __init__: Initializes a connection to a SQLite database and creates necessary tables.
            - create_tables: Creates tables for expenses and budget in the database. Initializes the budget if it does not exist.
            - add_expense: Adds a new expense to the database.
            - remove_expense: Remove an expense from the database using the provided expense ID.
            - add_budget: Add the specified amount to the current budget in the database.
            - get_current_budget: Retrieves the current budget amount from the database.
            - get_expenses: Retrieves all expenses from the database.
            - view_monthly_info: View the monthly information including total expenses and detailed expense breakdown.
            - clear: Clears all data from the tables in the SQLite database.
            - close: Closes the connection.

            Attributes:
            - connection: Represents the connection to the SQLite database.
            - cursor: Represents the cursor object for executing SQL queries.
            - expenses: table for storing expenses with columns id (INTEGER PRIMARY KEY AUTOINCREMENT), amount (REAL), category (TEXT), description (TEXT)
            - budget: table for storing budget with columns id (INTEGER PRIMARY KEY), amount (REAL)
    """
    def __init__(self):
        """
        Initializes a connection to a SQLite database, creates necessary tables, and sets up the cursor for executing SQL queries. The method establishes a connection to the 'budget.db' SQLite database, initializes the cursor object for query execution, and then calls the create_tables method to create essential tables in the database.
        """
        self.connection = sqlite3.connect('budget.db')
        self.cursor = self.connection.cursor()  # Здесь нужно использовать cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates tables for expenses and budget in the database. Initializes the budget table if it does not exist.

        Args:
            None

        Class Fields Initialized:
        - expenses: table for storing expenses with columns id (INTEGER PRIMARY KEY AUTOINCREMENT), amount (REAL), category (TEXT), description (TEXT)
        - budget: table for storing budget with columns id (INTEGER PRIMARY KEY), amount (REAL)
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
        Adds a new expense to the database with the provided amount, category, and description by executing an SQL query to insert the expense details into the expenses table. Subsequently, commits the changes to the database to ensure persistence.
        """
        self.cursor.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)', 
                            (amount, category, description))
        self.connection.commit()

    def remove_expense(self, expense_id):
        """
        Remove an expense from the database using the provided expense ID.

        Args:
        - expense_id: The unique identifier of the expense to be removed.

        The method executes a SQL DELETE query to remove the expense with the specified ID from the 'expenses' table in the database. Subsequently, it commits the changes to ensure the deletion is finalized.
        """
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.connection.commit()

    def add_budget(self, amount):
        """
        Add the specified amount to the current budget in the database and update the database accordingly.

        Args:
        - amount: The amount to be added to the current budget.

        The method retrieves the current budget from the database, adds the specified amount to it, updates the budget in the database, and commits the changes.
        """
        current_budget = self.get_current_budget()
        new_budget = current_budget + amount
        self.cursor.execute('UPDATE budget SET amount = ? WHERE id = 1', (new_budget,))
        self.connection.commit()

    def get_current_budget(self):
        """
        Retrieves the current budget amount from the database.

        Args:
            self: The Database object instance.

        The method executes a SQL query to select the 'amount' column from the 'budget' table where the 'id' is 1. It then fetches the first result and returns the current budget amount as a float.
        """
        self.cursor.execute('SELECT amount FROM budget WHERE id = 1')
        return self.cursor.fetchone()[0]

    def get_expenses(self):
        """
        Retrieves all expenses from the database as a list of tuples. Each tuple contains the expense ID, date, category, and amount.
        """
        self.cursor.execute('SELECT * FROM expenses')
        return [(row[0], row[1], row[2], row[3]) for row in self.cursor.fetchall()]

    def view_monthly_info(self):
        """
        View the monthly information including total expenses and detailed expense breakdown.

        Args:
            - No parameters.

        Returns:
            A formatted string containing the total expenses and a breakdown of individual expenses, including the amount and description for each expense.
        """
        expenses = self.get_expenses()
        total_expenses = sum(exp[1] for exp in expenses)
        
        info = f"Total Expenses: ${total_expenses:.2f}\n"
        info += "\n".join([f"{exp[1]} - {exp[2]}: {exp[3]}" for exp in expenses])
        
        return info

    def clear(self):
        """
        Clears all data from the tables in the SQLite database by executing SQL queries to delete all records from each table and resetting the auto-increment counters. Commits the changes to the database after clearing the data.
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f"DELETE FROM {table[0]};")
            self.cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table[0]}';")
        self.connection.commit()

    def close(self):
        """
        Closes the connection to the database.
        """
        self.connection.close()
