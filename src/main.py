```python
"""
Main application entry point.
"""

import logging
import sys

from src.config import Config
from src.database import Database
from src.services import UserService

def main():
    """
    Main application entry point.
    
    Initializes the application, sets up logging, and starts the main loop.
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Initialize the application
    config = Config()
    database = Database(config.database_url)
    user_service = UserService(database)
    
    # Start the main loop
    while True:
        try:
            # Handle user input
            user_input = input("Enter a command (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            user_service.handle_input(user_input)
        except Exception as e:
            logging.error(f"Error handling user input: {e}")

if __name__ == "__main__":
    main()
```