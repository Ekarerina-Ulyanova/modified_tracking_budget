```python
import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('budget.db')
        self.cursor = self.connection.cursor()  # Здесь нужно использовать cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''\
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT
            )
        ''')
        
        self.cursor.execute('''\
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

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Insert a new expense into the database."""
        self.cursor.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)', 
                            (amount, category, description))
        self.connection.commit()

    def remove_expense(self, expense_id: int) -> None:
        """Remove an expense from the database by its ID."""
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.connection.commit()

    def add_budget(self, amount: float) -> None:
        """Update the current budget by adding a new amount."""
        current_budget = self.get_current_budget()
        new_budget = current_budget + amount
        self.cursor.execute('UPDATE budget SET amount = ? WHERE id = 1', (new_budget,))
        self.connection.commit()

    def get_current_budget(self) -> float:
        """Retrieve the current budget from the database."""
        self.cursor.execute('SELECT amount FROM budget WHERE id = 1')
        return self.cursor.fetchone()[0]

    def get_expenses(self) -> list[tuple[int, float, str, str]]:
        """Retrieve all expenses from the database."""
        self.cursor.execute('SELECT * FROM expenses')
        return [(row[0], row[1], row[2], row[3]) for row in self.cursor.fetchall()]

    def view_monthly_info(self) -> str:
        """Retrieve and display monthly information, including total expenses and individual expenses."""
        expenses = self.get_expenses()
        total_expenses = sum(exp[1] for exp in expenses)
        
        info = f"Total Expenses: ${total_expenses:.2f}\n"
        info += "\n".join([f"{exp[1]} - {exp[2]}: {exp[3]}" for exp in expenses])
        
        return info

    def clear(self) -> None:
        """Clear all data from the database."""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f"DELETE FROM {table[0]};")
            self.cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table[0]}';")
        self.connection.commit()

    def close(self) -> None:
        """Close the database connection."""
        self.connection.close()
```