"""
Preston's Kitchen - Main Flask Application
A kitchen inventory tracker for pantry and fridge items
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import init_db, get_db
from models import Item
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DATABASE'] = 'kitchen_inventory.db'

# Initialize database on first run
with app.app_context():
    init_db()


# ============================================================================
# ROUTES - Main Pages
# ============================================================================

@app.route('/')
def index():
    """
    Main inventory view showing both Pantry and Fridge sections

    TODO: Implement the following:
    1. Query all items from the database
    2. Separate items into pantry_items and fridge_items based on category
    3. Pass both lists to the template
    4. Handle any database errors gracefully
    """
    # TODO: Get items from database
    pantry_items = []  # Replace with actual query
    fridge_items = []  # Replace with actual query

    return render_template('index.html',
                         pantry_items=pantry_items,
                         fridge_items=fridge_items)


# ============================================================================
# API ROUTES - Item Management
# ============================================================================

@app.route('/api/items', methods=['GET'])
def get_items():
    """
    Get all items, optionally filtered by category
    Query params: ?category=pantry or ?category=fridge

    TODO: Implement the following:
    1. Get the 'category' query parameter from request.args
    2. Query items from database (all items or filtered by category)
    3. Convert items to dictionaries using to_dict() method
    4. Return JSON response with items list
    """
    # TODO: Implement GET items logic
    return jsonify({'items': []})


@app.route('/api/items', methods=['POST'])
def add_item():
    """
    Add a new item to inventory
    Expects JSON: {"name": "Milk", "category": "fridge", "status": "plenty"}

    TODO: Implement the following:
    1. Get JSON data from request
    2. Validate required fields (name, category)
    3. Set default status to "plenty" if not provided
    4. Create new Item object
    5. Save to database
    6. Return success response with created item data
    7. Handle validation errors (return 400 status)
    """
    # TODO: Implement POST item logic
    return jsonify({'error': 'Not implemented'}), 501


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Update an existing item (mainly for status changes)
    Expects JSON: {"status": "running_low"}

    TODO: Implement the following:
    1. Get the item from database by item_id
    2. If item not found, return 404 error
    3. Get JSON data from request
    4. Update item fields (status, name, category if provided)
    5. Save changes to database
    6. Return updated item data
    """
    # TODO: Implement PUT item logic
    return jsonify({'error': 'Not implemented'}), 501


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Delete an item from inventory

    TODO: Implement the following:
    1. Get the item from database by item_id
    2. If item not found, return 404 error
    3. Delete the item from database
    4. Return success response
    """
    # TODO: Implement DELETE item logic
    return jsonify({'error': 'Not implemented'}), 501


@app.route('/api/items/<int:item_id>/status', methods=['PATCH'])
def update_item_status(item_id):
    """
    Quick endpoint to toggle/update just the status of an item
    Expects JSON: {"status": "out"}

    TODO: Implement the following:
    1. Get the item from database by item_id
    2. Get new status from request JSON
    3. Validate status is one of: "plenty", "running_low", "out"
    4. Update item status
    5. Save to database
    6. Return updated item
    """
    # TODO: Implement PATCH status logic
    return jsonify({'error': 'Not implemented'}), 501


# ============================================================================
# UTILITY ROUTES
# ============================================================================

@app.route('/api/shopping-list')
def get_shopping_list():
    """
    Get items that are "out" or "running_low" to create a shopping list

    TODO: Implement the following:
    1. Query items where status is "out" or "running_low"
    2. Group by category for easier shopping
    3. Return JSON with categorized shopping list
    """
    # TODO: Implement shopping list logic
    return jsonify({'shopping_list': []})


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Not found'}), 404
    return render_template('index.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Internal server error'}), 500
    return render_template('index.html'), 500


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == '__main__':
    # Run in debug mode for development
    # Set debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5000)
