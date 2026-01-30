```python
from database import Database

class TestDatabase:
    """
    A class for testing the Database class.
    """

    def test_database_connection(self):
        """
        Test the connection to the database.
        
        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        db = Database()
        return db.connect()

    def test_database_insert(self):
        """
        Test the insertion of data into the database.
        
        Returns:
            bool: True if the insertion is successful, False otherwise.
        """
        db = Database()
        return db.insert("test_data")

    def test_database_query(self):
        """
        Test the querying of data from the database.
        
        Returns:
            list: A list of query results.
        """
        db = Database()
        return db.query("SELECT * FROM test_table")

    def test_database_close(self):
        """
        Test the closing of the database connection.
        
        Returns:
            bool: True if the connection is closed successfully, False otherwise.
        """
        db = Database()
        return db.close()

def main():
    """
    Run the tests for the Database class.
    """
    test_db = TestDatabase()
    print("Testing database connection:", test_db.test_database_connection())
    print("Testing database insertion:", test_db.test_database_insert())
    print("Testing database query:", test_db.test_database_query())
    print("Testing database close:", test_db.test_database_close())

if __name__ == "__main__":
    main()
```