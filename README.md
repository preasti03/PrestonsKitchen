# Preston's Kitchen

A mobile-friendly kitchen inventory tracker to manage pantry and fridge items with simple status tracking.

## Project Overview

Preston's Kitchen helps you keep track of what's in your kitchen and what you need to buy. Items have three status levels:
- **Plenty** - Well stocked
- **Running Low** - Need to buy soon
- **Out** - Need to buy

### MVP Features
- Separate tracking for Pantry and Fridge items
- Three-level status system
- Quick status updates with tap/click
- Mobile-responsive design for grocery store use
- Shopping list generation from items marked "Out" or "Running Low"

### Future Enhancements
- LLM integration for smart shopping list generation
- Recipe suggestions based on available ingredients
- Expiration date tracking
- Barcode scanning

## Tech Stack

- **Backend**: Python 3.x with Flask
- **Database**: SQLite (file-based, no server required)
- **Frontend**: HTML5, CSS3 (vanilla), JavaScript (vanilla)
- **Deployment**: Render (free tier) - see deployment guide below

## Project Structure

```
PrestonsKitchen/
├── app.py                  # Main Flask application with routes
├── models.py               # Database models (Item class)
├── database.py             # Database initialization and helpers
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
├── README.md              # This file
├── static/
│   ├── css/
│   │   └── style.css      # All styles (mobile-first design)
│   └── js/
│       └── main.js        # Frontend JavaScript
└── templates/
    ├── base.html          # Base template with common HTML
    ├── index.html         # Main inventory view
    └── components/
        └── item_card.html # Reusable item card component
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for version control)

### Local Development Setup

1. **Clone or navigate to the project directory**
   ```bash
   cd PrestonsKitchen
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   On Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to: `http://localhost:5000`

### First Time Setup Checklist

Before the app will work, you need to implement the TODO items in these files:

#### Priority 1 - Database (Required for app to start)
- [ ] `database.py`: Implement `get_db()` function
- [ ] `database.py`: Implement `close_db()` function
- [ ] `database.py`: Implement `init_db()` function to create tables

#### Priority 2 - Models (Required for data operations)
- [ ] `models.py`: Implement `Item.__init__()` with validation
- [ ] `models.py`: Implement `Item.save()` for INSERT/UPDATE
- [ ] `models.py`: Implement `Item.get_all()` class method
- [ ] `models.py`: Implement `Item.get_by_id()` class method

#### Priority 3 - API Routes (Required for frontend to work)
- [ ] `app.py`: Implement `index()` route to display items
- [ ] `app.py`: Implement `add_item()` POST route
- [ ] `app.py`: Implement `update_item_status()` PATCH route
- [ ] `app.py`: Implement `delete_item()` DELETE route
- [ ] `app.py`: Implement `get_shopping_list()` route

#### Priority 4 - Frontend JavaScript (Required for interactivity)
- [ ] `main.js`: Implement `showAddItemModal()` function
- [ ] `main.js`: Implement `closeModal()` function
- [ ] `main.js`: Implement `addItem()` form submission
- [ ] `main.js`: Implement `updateItemStatus()` function
- [ ] `main.js`: Implement `deleteItem()` function
- [ ] `main.js`: Implement `showShoppingList()` function

#### Optional Enhancements
- [ ] Add sample data in `database.py` for testing
- [ ] Implement quick-add buttons for common items
- [ ] Add loading states and animations
- [ ] Implement toast notifications instead of alerts
- [ ] Add search/filter functionality
- [ ] Improve accessibility (ARIA labels, keyboard navigation)

## Architecture Guide

### Database Layer (`database.py`)

The database layer handles all SQLite interactions:

- **`get_db()`**: Returns a database connection for the current request
  - Uses Flask's `g` object to store connection per request
  - Prevents connection leaks and threading issues

- **`init_db()`**: Creates tables on first run
  - Safe to run multiple times (uses IF NOT EXISTS)
  - Creates indexes for better query performance

- **Helper functions**: `query_db()` and `execute_db()`
  - Simplify common database operations
  - Used by models.py

### Models Layer (`models.py`)

The `Item` class represents inventory items:

**Attributes:**
- `id`: Unique identifier (auto-incremented)
- `name`: Item name (e.g., "Milk")
- `category`: "pantry" or "fridge"
- `status`: "plenty", "running_low", or "out"
- `created_at`: Timestamp when item was added
- `updated_at`: Timestamp of last modification

**Instance Methods:**
- `save()`: Insert new item or update existing
- `delete()`: Remove item from database
- `to_dict()`: Convert to dictionary for JSON responses

**Class Methods:**
- `get_all(category=None)`: Fetch all items, optionally filtered
- `get_by_id(id)`: Fetch single item by ID
- `get_by_status(status)`: Fetch items with specific status
- `get_shopping_list()`: Fetch items that need purchasing

### Application Layer (`app.py`)

Flask routes handle HTTP requests and responses:

**Page Routes:**
- `GET /`: Main inventory view

**API Routes:**
- `GET /api/items`: Get all items (with optional ?category= filter)
- `POST /api/items`: Create new item
- `PUT /api/items/<id>`: Update existing item
- `PATCH /api/items/<id>/status`: Quick status update
- `DELETE /api/items/<id>`: Delete item
- `GET /api/shopping-list`: Get items to purchase

### Frontend

**Templates** (`templates/`):
- `base.html`: Common HTML structure, headers, scripts
- `index.html`: Main inventory page with Pantry and Fridge sections
- `components/item_card.html`: Reusable item display component

**JavaScript** (`static/js/main.js`):
- API communication functions (fetch, create, update, delete)
- Modal management
- DOM manipulation
- Event handling

**CSS** (`static/css/style.css`):
- Mobile-first responsive design
- CSS variables for easy theming
- Component-based organization
- Accessible design (focus states, contrast)

## Development Workflow

### Recommended Implementation Order

1. **Database Setup**
   - Implement database.py functions
   - Test with Python REPL or add sample data
   - Verify tables are created correctly

2. **Models**
   - Implement Item class methods
   - Test with Python REPL
   - Ensure validation works

3. **Backend Routes**
   - Start with GET routes (read operations)
   - Test with browser or curl
   - Implement POST/PATCH/DELETE (write operations)
   - Test with Postman or curl

4. **Frontend Integration**
   - Implement JavaScript API functions
   - Connect modal and form handling
   - Test add/update/delete workflows
   - Polish UI/UX

### Testing Tips

**Test the database:**
```python
# In Python REPL
python
>>> from database import init_db, get_db
>>> from app import app
>>> with app.app_context():
...     init_db()
...     db = get_db()
...     cursor = db.execute("SELECT * FROM items")
...     print(cursor.fetchall())
```

**Test API routes with curl:**
```bash
# Get all items
curl http://localhost:5000/api/items

# Add an item
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Milk","category":"fridge","status":"running_low"}'

# Update status
curl -X PATCH http://localhost:5000/api/items/1/status \
  -H "Content-Type: application/json" \
  -d '{"status":"out"}'

# Delete an item
curl -X DELETE http://localhost:5000/api/items/1
```

**Test in browser:**
- Use browser DevTools Console for JavaScript debugging
- Check Network tab to see API requests/responses
- Use Elements tab to inspect CSS

## Deployment to Render

### Preparation

1. **Add a `Procfile`** (tells Render how to run your app):
   ```
   web: gunicorn app:app
   ```

2. **Update app.py** for production:
   ```python
   if __name__ == '__main__':
       app.run(debug=False)  # Set debug=False for production
   ```

3. **Set environment variable for SECRET_KEY** in Render dashboard

### Steps

1. Create account on [Render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variable: `SECRET_KEY=your-secret-key-here`
6. Deploy!

## Learning Resources

### Flask
- [Flask Official Tutorial](https://flask.palletsprojects.com/tutorial/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### SQLite
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python SQLite3 Docs](https://docs.python.org/3/library/sqlite3.html)

### HTML/CSS
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web)
- [CSS Tricks](https://css-tricks.com/)
- [Responsive Design Basics](https://web.dev/responsive-web-design-basics/)

### JavaScript
- [JavaScript.info](https://javascript.info/)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## Git Best Practices

Initialize git repository:
```bash
git init
git add .
git commit -m "Initial commit: Preston's Kitchen skeleton"
```

Create feature branches:
```bash
git checkout -b feature/database-implementation
# Make changes
git add .
git commit -m "Implement database initialization and helpers"
git checkout main
git merge feature/database-implementation
```

## Troubleshooting

### Database Issues
- **Error: "table already exists"**: This is safe to ignore if you're running init_db() multiple times
- **Error: "no such table"**: Run init_db() to create tables
- **Data not persisting**: Check that db.commit() is called after writes

### Flask Issues
- **Port already in use**: Change port in app.py or kill the existing process
- **Template not found**: Check that templates are in the templates/ folder
- **Static files not loading**: Check that static files are in the static/ folder

### JavaScript Issues
- **API calls failing**: Check browser console and Network tab
- **CORS errors**: Shouldn't happen since frontend and backend are same origin
- **Functions not defined**: Ensure main.js is loaded in base.html

## License

This is a personal learning project. Feel free to use and modify as needed.

## Next Steps

Once you've implemented the MVP:

1. Test thoroughly on mobile devices
2. Add your own custom features
3. Deploy to Render
4. Share with friends/family
5. Iterate based on feedback

Happy coding! 🍳
