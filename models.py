"""
Database models for Preston's Kitchen
Defines the Item class for pantry and fridge inventory
"""

from database import query_db, execute_db
from datetime import datetime


class Item:
    """
    Represents a single inventory item (pantry or fridge)

    Attributes:
        id (int): Unique identifier
        name (str): Item name (e.g., "Milk", "Flour")
        category (str): Either "pantry" or "fridge"
        status (str): One of "plenty", "running_low", "out"
        created_at (datetime): When item was added
        updated_at (datetime): When item was last modified
    """

    # Valid values for category and status
    VALID_CATEGORIES = ['pantry', 'fridge']
    VALID_STATUSES = ['plenty', 'running_low', 'out']

    def __init__(self, name, category, status='plenty', id=None, created_at=None, updated_at=None):
        """
        Initialize a new Item

        TODO: Implement the following:
        1. Validate category is in VALID_CATEGORIES
        2. Validate status is in VALID_STATUSES
        3. Set all attributes (id, name, category, status, timestamps)
        4. Raise ValueError if validation fails

        Args:
            name: Item name
            category: 'pantry' or 'fridge'
            status: 'plenty', 'running_low', or 'out' (defaults to 'plenty')
            id: Database ID (None for new items)
            created_at: Creation timestamp
            updated_at: Last update timestamp
        """
        # TODO: Validate and set attributes

        if category not in self.VALID_CATEGORIES:
            raise ValueError(f"Invalid category: {category}. Must be one of {self.VALID_CATEGORIES}")

        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}. Must be one of {self.VALID_STATUSES}")
        
        self.id = id
        self.name = name
        self.category = category
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        """
        Save the item to database (INSERT if new, UPDATE if exists)

        TODO: Implement the following:
        1. Check if self.id is None (new item) or exists (update)
        2. For new items:
           - INSERT into database
           - Set self.id to the returned last row ID
        3. For existing items:
           - UPDATE the database record
           - Update the updated_at timestamp
        4. Return self for method chaining

        Hint: Use execute_db() from database.py
        """
        # TODO: Implement save logic
        if self.id is None:
            # INSERT new item
            self.id = execute_db('''
                                 INSERT INTO items (name, category, status)
                                 VALUES (?, ?, ?)
            ''', (self.name, self.category, self.status))
        else:
            # UPDATE existing item
            execute_db('''
                       UPDATE items
                       SET name = ?, category = ?, status = ?, updated_at = CURRENT_TIMESTAMP
                       WHERE id = ?
                       ''', (self.name, self.category, self.status, self.id))

        return self

    def delete(self):
        """
        Delete this item from the database

        TODO: Implement the following:
        1. Check if item has an ID (can't delete unsaved item)
        2. Execute DELETE query
        3. Set self.id to None (item no longer in database)
        4. Return True if successful

        Hint: Use execute_db() from database.py
        """
        # TODO: Implement delete logic
        if self.id is None:
            return False

        # Your code here
        return True

    def to_dict(self):
        """
        Convert item to dictionary for JSON serialization

        TODO: Implement the following:
        1. Create dictionary with all item attributes
        2. Convert datetime objects to ISO format strings
        3. Return the dictionary

        Returns:
            dict: Item data as dictionary
        """
        # TODO: Implement to_dict conversion
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def from_db_row(row):
        """
        Create an Item object from a database row

        TODO: Implement the following:
        1. Extract values from row (dict-like object)
        2. Create and return new Item instance with these values

        Args:
            row: Database row (sqlite3.Row object)

        Returns:
            Item: New Item instance
        """
        # TODO: Create Item from database row
        if row is None:
            return None

        return Item(
            id=row['id'],
            name=row['name'],
            category=row['category'],
            status=row['status'],
            created_at=row['created_at'],
            updated_at=row['updated_at']
        )

    # ========================================================================
    # CLASS METHODS - Query Operations
    # ========================================================================

    @classmethod
    def get_all(cls, category=None):
        """
        Get all items, optionally filtered by category

        TODO: Implement the following:
        1. Build SQL query to SELECT all items
        2. If category provided, add WHERE clause
        3. Execute query using query_db()
        4. Convert each row to Item object using from_db_row()
        5. Return list of Item objects

        Args:
            category: Optional category filter ('pantry' or 'fridge')

        Returns:
            list[Item]: List of Item objects
        """
        # TODO: Implement get_all query
        if category:
            # Query with category filter
            query = 'SELECT * FROM items WHERE category = ? ORDER BY name'
            rows = query_db(query, (category,))
        else:
            # Query all items
            query = 'SELECT * FROM items ORDER BY name'
            rows = query_db(query) 

        return [cls.from_db_row(row) for row in rows]

    @classmethod
    def get_by_id(cls, item_id):
        """
        Get a single item by ID

        TODO: Implement the following:
        1. Query database for item with given ID
        2. Use query_db() with one=True
        3. Convert row to Item object using from_db_row()
        4. Return Item or None if not found

        Args:
            item_id: Item ID to find

        Returns:
            Item or None: Item object if found, None otherwise
        """
        # TODO: Implement get_by_id query
        query = 'SELECT * FROM items WHERE id = ?'
        row = query_db(query, (item_id,), one=True)

        return cls.from_db_row(row) if row else None

    @classmethod
    def get_by_status(cls, status, category=None):
        """
        Get items by status, optionally filtered by category

        TODO: Implement the following:
        1. Validate status is in VALID_STATUSES
        2. Build query to find items with given status
        3. If category provided, add to WHERE clause
        4. Execute query and convert rows to Item objects
        5. Return list of items

        Args:
            status: Status to filter by ('plenty', 'running_low', 'out')
            category: Optional category filter

        Returns:
            list[Item]: List of matching items
        """
        # TODO: Implement get_by_status query
        return []

    @classmethod
    def get_shopping_list(cls):
        """
        Get items that need to be purchased (status: 'out' or 'running_low')

        TODO: Implement the following:
        1. Query items where status is 'out' OR 'running_low'
        2. Order by category, then by name for organized shopping
        3. Convert to Item objects
        4. Return list

        Returns:
            list[Item]: Items that need to be purchased
        """
        # TODO: Implement shopping list query
        return []

    def __repr__(self):
        """String representation of Item for debugging"""
        return f"<Item {self.id}: {self.name} ({self.category}) - {self.status}>"

    def __str__(self):
        """Human-readable string representation"""
        return f"{self.name} [{self.status}]"
