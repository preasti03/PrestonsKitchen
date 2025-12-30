"""
Database initialization and helper functions for Preston's Kitchen
Uses SQLite for simple, file-based storage
"""

import sqlite3
from flask import g
from flask import current_app


def get_db():
    """
    Get database connection for the current request
    Creates a new connection if one doesn't exist

    Flask's 'g' object stores data specific to the current request.
    This ensures each request gets its own database connection.

    TODO: Implement the following:
    1. Check if 'db' exists in g object
    2. If not, create new SQLite connection to current_app.config['DATABASE']
    3. Set row_factory to sqlite3.Row for dict-like access
    4. Store connection in g.db
    5. Return the connection

    Hint: Use sqlite3.connect() to create connection
    """
    # TODO: Implement database connection logic
    if 'db' not in g:
        # Your code here
        pass

    return g.db


def close_db(e=None):
    """
    Close database connection at the end of the request

    TODO: Implement the following:
    1. Pop 'db' from g object (returns None if doesn't exist)
    2. If db exists, close the connection
    """
    # TODO: Implement database closing logic
    db = g.pop('db', None)

    if db is not None:
        # Your code here
        pass


def init_db():
    """
    Initialize the database with required tables
    Creates the 'items' table if it doesn't exist

    TODO: Implement the following:
    1. Get database connection
    2. Create 'items' table with these columns:
       - id: INTEGER PRIMARY KEY AUTOINCREMENT
       - name: TEXT NOT NULL
       - category: TEXT NOT NULL (pantry or fridge)
       - status: TEXT NOT NULL (plenty, running_low, out)
       - created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       - updated_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    3. Create index on category for faster queries
    4. Commit the changes

    Hint: Use multi-line SQL string with triple quotes
    Hint: Use IF NOT EXISTS to make this safe to run multiple times
    """
    db = get_db()

    # TODO: Create table schema
    # Example structure:
    # db.execute('''
    #     CREATE TABLE IF NOT EXISTS items (
    #         -- Your columns here
    #     )
    # ''')
    #
    # db.execute('CREATE INDEX IF NOT EXISTS idx_category ON items(category)')
    #
    # db.commit()

    print("Database initialized successfully")


def query_db(query, args=(), one=False):
    """
    Utility function to query the database

    Args:
        query: SQL query string
        args: Tuple of query parameters
        one: If True, return single result; if False, return all results

    Returns:
        Single row if one=True, list of rows if one=False

    TODO: Implement the following:
    1. Get database connection
    2. Execute query with args
    3. Fetch all results
    4. Return single result if one=True, otherwise return all
    5. Handle any exceptions gracefully

    This is a helper function you can use in models.py
    """
    # TODO: Implement query helper
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def execute_db(query, args=()):
    """
    Utility function to execute INSERT, UPDATE, DELETE queries

    Args:
        query: SQL query string
        args: Tuple of query parameters

    Returns:
        Last inserted row ID (useful for INSERT operations)

    TODO: Implement the following:
    1. Get database connection
    2. Execute query with args
    3. Commit the transaction
    4. Return lastrowid from cursor

    This is a helper function you can use in models.py
    """
    # TODO: Implement execute helper
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    last_id = cur.lastrowid
    cur.close()
    return last_id


# ============================================================================
# SAMPLE DATA (Optional - for testing)
# ============================================================================

def add_sample_data():
    """
    Add sample items to the database for testing
    Only use this during development!

    TODO (Optional): Implement this function to add test data
    1. Create a few sample pantry items
    2. Create a few sample fridge items
    3. Use different status values to test UI

    You can call this from app.py after init_db() during development
    """
    # TODO: Add sample items
    sample_items = [
        # ('Flour', 'pantry', 'plenty'),
        # ('Milk', 'fridge', 'running_low'),
        # Add more sample items
    ]

    # for name, category, status in sample_items:
    #     execute_db(
    #         'INSERT INTO items (name, category, status) VALUES (?, ?, ?)',
    #         (name, category, status)
    #     )

    print("Sample data added")
