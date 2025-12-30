/**
 * Preston's Kitchen - Main JavaScript
 * Handles all interactive features and API communication
 *
 * TODO: Implement all functions marked with TODO
 * TODO: Add error handling and user feedback (toasts/alerts)
 * TODO: Consider adding loading states for better UX
 */

// ============================================================================
// GLOBAL STATE (Optional - you can manage state differently)
// ============================================================================

let currentItems = {
    pantry: [],
    fridge: []
};

// ============================================================================
// INITIALIZATION
// ============================================================================

/**
 * Initialize the application when DOM is ready
 * TODO: Implement initialization logic
 * - Load items from API
 * - Set up event listeners
 * - Initialize any plugins or components
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Preston\'s Kitchen initialized');

    // TODO: Load initial data
    // loadItems();

    // TODO: Set up event listeners
    // setupEventListeners();
});

// ============================================================================
// API COMMUNICATION
// ============================================================================

/**
 * Fetch all items from the API
 * TODO: Implement the following:
 * 1. Make GET request to /api/items
 * 2. Optionally filter by category (?category=pantry or ?category=fridge)
 * 3. Update currentItems state
 * 4. Return the items
 * 5. Handle errors gracefully
 *
 * @param {string} category - Optional: 'pantry' or 'fridge'
 * @returns {Promise<Array>} Array of items
 */
async function loadItems(category = null) {
    try {
        // TODO: Implement API call
        // const url = category ? `/api/items?category=${category}` : '/api/items';
        // const response = await fetch(url);
        // const data = await response.json();
        // return data.items;

        console.log('TODO: Implement loadItems()');
        return [];
    } catch (error) {
        console.error('Error loading items:', error);
        showError('Failed to load items');
        return [];
    }
}

/**
 * Create a new item via API
 * TODO: Implement the following:
 * 1. Make POST request to /api/items
 * 2. Send JSON body with { name, category, status }
 * 3. Handle response (success or error)
 * 4. Refresh the items list
 * 5. Show success message to user
 *
 * @param {Object} itemData - { name, category, status }
 * @returns {Promise<Object>} Created item
 */
async function createItem(itemData) {
    try {
        // TODO: Implement API call
        // const response = await fetch('/api/items', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(itemData)
        // });
        //
        // if (!response.ok) {
        //     throw new Error('Failed to create item');
        // }
        //
        // const data = await response.json();
        // return data;

        console.log('TODO: Implement createItem()', itemData);
        return null;
    } catch (error) {
        console.error('Error creating item:', error);
        showError('Failed to create item');
        throw error;
    }
}

/**
 * Update an item's status via API
 * TODO: Implement the following:
 * 1. Make PATCH request to /api/items/{id}/status
 * 2. Send JSON body with { status }
 * 3. Handle response
 * 4. Update the UI to reflect new status
 * 5. Show feedback to user
 *
 * @param {number} itemId - ID of item to update
 * @param {string} newStatus - 'plenty', 'running_low', or 'out'
 * @returns {Promise<Object>} Updated item
 */
async function updateStatus(itemId, newStatus) {
    try {
        // TODO: Implement API call
        // const response = await fetch(`/api/items/${itemId}/status`, {
        //     method: 'PATCH',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ status: newStatus })
        // });
        //
        // if (!response.ok) {
        //     throw new Error('Failed to update status');
        // }
        //
        // const data = await response.json();
        // return data;

        console.log(`TODO: Implement updateStatus() - Item ${itemId} -> ${newStatus}`);
        return null;
    } catch (error) {
        console.error('Error updating status:', error);
        showError('Failed to update status');
        throw error;
    }
}

/**
 * Delete an item via API
 * TODO: Implement the following:
 * 1. Show confirmation dialog to user
 * 2. Make DELETE request to /api/items/{id}
 * 3. Handle response
 * 4. Remove item from UI
 * 5. Show success message
 *
 * @param {number} itemId - ID of item to delete
 * @returns {Promise<boolean>} Success status
 */
async function deleteItemAPI(itemId) {
    try {
        // TODO: Implement confirmation dialog
        // if (!confirm('Are you sure you want to delete this item?')) {
        //     return false;
        // }

        // TODO: Implement API call
        // const response = await fetch(`/api/items/${itemId}`, {
        //     method: 'DELETE'
        // });
        //
        // if (!response.ok) {
        //     throw new Error('Failed to delete item');
        // }
        //
        // return true;

        console.log(`TODO: Implement deleteItemAPI() - Item ${itemId}`);
        return false;
    } catch (error) {
        console.error('Error deleting item:', error);
        showError('Failed to delete item');
        throw error;
    }
}

/**
 * Fetch shopping list from API
 * TODO: Implement the following:
 * 1. Make GET request to /api/shopping-list
 * 2. Return items that are 'out' or 'running_low'
 * 3. Group by category for easier shopping
 *
 * @returns {Promise<Object>} Shopping list data
 */
async function fetchShoppingList() {
    try {
        // TODO: Implement API call
        // const response = await fetch('/api/shopping-list');
        // const data = await response.json();
        // return data.shopping_list;

        console.log('TODO: Implement fetchShoppingList()');
        return { pantry: [], fridge: [] };
    } catch (error) {
        console.error('Error fetching shopping list:', error);
        showError('Failed to load shopping list');
        return { pantry: [], fridge: [] };
    }
}

// ============================================================================
// UI INTERACTIONS - Modal Management
// ============================================================================

/**
 * Show the "Add Item" modal
 * TODO: Implement the following:
 * 1. Set the modal title based on category
 * 2. Set the hidden category input value
 * 3. Clear the form
 * 4. Add 'active' class to modal to show it
 * 5. Focus on the name input field
 *
 * @param {string} category - 'pantry' or 'fridge'
 */
function showAddItemModal(category) {
    // TODO: Implement modal display logic
    // const modal = document.getElementById('add-item-modal');
    // const title = document.getElementById('modal-title');
    // const categoryInput = document.getElementById('item-category');
    // const nameInput = document.getElementById('item-name');
    //
    // title.textContent = `Add ${category.charAt(0).toUpperCase() + category.slice(1)} Item`;
    // categoryInput.value = category;
    // nameInput.value = '';
    //
    // modal.classList.add('active');
    // nameInput.focus();

    console.log(`TODO: Implement showAddItemModal('${category}')`);
}

/**
 * Close a modal
 * TODO: Implement the following:
 * 1. Get modal element by ID
 * 2. Remove 'active' class
 * 3. Clear any form data if needed
 *
 * @param {string} modalId - ID of modal to close
 */
function closeModal(modalId) {
    // TODO: Implement modal close logic
    // const modal = document.getElementById(modalId);
    // modal.classList.remove('active');
    //
    // // Clear form if it's the add-item-modal
    // if (modalId === 'add-item-modal') {
    //     document.getElementById('add-item-form').reset();
    // }

    console.log(`TODO: Implement closeModal('${modalId}')`);
}

/**
 * Close modal when clicking outside of it
 * TODO: Add event listener to modal background
 */
window.onclick = function(event) {
    // TODO: Implement click-outside-to-close logic
    // if (event.target.classList.contains('modal')) {
    //     event.target.classList.remove('active');
    // }
};

// ============================================================================
// UI INTERACTIONS - Item Management
// ============================================================================

/**
 * Handle add item form submission
 * TODO: Implement the following:
 * 1. Prevent default form submission
 * 2. Get form data (name, category, status)
 * 3. Validate data
 * 4. Call createItem() API function
 * 5. On success:
 *    - Close modal
 *    - Refresh items list OR add item to DOM directly
 *    - Show success message
 * 6. On error:
 *    - Show error message
 *    - Keep modal open
 *
 * @param {Event} event - Form submit event
 */
async function addItem(event) {
    // TODO: Implement form submission logic
    // event.preventDefault();
    //
    // const form = event.target;
    // const formData = new FormData(form);
    //
    // const itemData = {
    //     name: formData.get('name'),
    //     category: formData.get('category'),
    //     status: formData.get('status')
    // };
    //
    // try {
    //     const newItem = await createItem(itemData);
    //     closeModal('add-item-modal');
    //     // Refresh or add to DOM
    //     showSuccess('Item added successfully!');
    // } catch (error) {
    //     // Error already handled in createItem
    // }

    console.log('TODO: Implement addItem()');
}

/**
 * Update an item's status
 * Called when user clicks status button
 * TODO: Implement the following:
 * 1. Call updateStatus() API function
 * 2. Update the item card UI to reflect new status
 * 3. Update status badge and active button states
 * 4. Show brief feedback (e.g., flash animation)
 *
 * @param {number} itemId - ID of item to update
 * @param {string} newStatus - 'plenty', 'running_low', or 'out'
 */
async function updateItemStatus(itemId, newStatus) {
    // TODO: Implement status update logic
    // try {
    //     const updatedItem = await updateStatus(itemId, newStatus);
    //
    //     // Update UI
    //     const itemCard = document.querySelector(`[data-item-id="${itemId}"]`);
    //     if (itemCard) {
    //         // Update data attribute
    //         itemCard.setAttribute('data-status', newStatus);
    //
    //         // Update status badge
    //         const badge = itemCard.querySelector('.status-badge');
    //         badge.className = `status-badge status-${newStatus}`;
    //         badge.textContent = newStatus.replace('_', ' ').toUpperCase();
    //
    //         // Update active button
    //         itemCard.querySelectorAll('.status-btn').forEach(btn => {
    //             btn.classList.remove('active');
    //         });
    //         itemCard.querySelector(`.status-btn-${newStatus.replace('_', '-')}`).classList.add('active');
    //     }
    // } catch (error) {
    //     // Error already handled
    // }

    console.log(`TODO: Implement updateItemStatus(${itemId}, '${newStatus}')`);
}

/**
 * Delete an item
 * Called when user clicks delete button
 * TODO: Implement the following:
 * 1. Call deleteItemAPI() which includes confirmation
 * 2. On success:
 *    - Remove item card from DOM
 *    - Show success message
 * 3. On failure/cancel:
 *    - Show error or do nothing
 *
 * @param {number} itemId - ID of item to delete
 */
async function deleteItem(itemId) {
    // TODO: Implement delete logic
    // try {
    //     const success = await deleteItemAPI(itemId);
    //
    //     if (success) {
    //         // Remove from DOM
    //         const itemCard = document.querySelector(`[data-item-id="${itemId}"]`);
    //         if (itemCard) {
    //             itemCard.remove();
    //         }
    //
    //         showSuccess('Item deleted');
    //     }
    // } catch (error) {
    //     // Error already handled
    // }

    console.log(`TODO: Implement deleteItem(${itemId})`);
}

// ============================================================================
// SHOPPING LIST
// ============================================================================

/**
 * Show shopping list modal
 * TODO: Implement the following:
 * 1. Fetch shopping list data from API
 * 2. Populate modal with items grouped by category
 * 3. Show modal
 * 4. Add formatting for easy reading (checkboxes, etc.)
 */
async function showShoppingList() {
    // TODO: Implement shopping list display
    // const modal = document.getElementById('shopping-list-modal');
    // const content = document.getElementById('shopping-list-content');
    //
    // // Show loading state
    // content.innerHTML = '<p class="loading">Loading shopping list...</p>';
    // modal.classList.add('active');
    //
    // // Fetch data
    // const shoppingList = await fetchShoppingList();
    //
    // // Build HTML
    // let html = '';
    //
    // if (shoppingList.pantry.length > 0) {
    //     html += '<h4>Pantry</h4><ul>';
    //     shoppingList.pantry.forEach(item => {
    //         html += `<li>${item.name} - ${item.status}</li>`;
    //     });
    //     html += '</ul>';
    // }
    //
    // if (shoppingList.fridge.length > 0) {
    //     html += '<h4>Fridge</h4><ul>';
    //     shoppingList.fridge.forEach(item => {
    //         html += `<li>${item.name} - ${item.status}</li>`;
    //     });
    //     html += '</ul>';
    // }
    //
    // if (html === '') {
    //     html = '<p class="empty-state">No items to buy! Everything is well-stocked.</p>';
    // }
    //
    // content.innerHTML = html;

    console.log('TODO: Implement showShoppingList()');
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Show success message to user
 * TODO: Implement a toast notification or alert
 *
 * @param {string} message - Success message
 */
function showSuccess(message) {
    // TODO: Implement success notification
    // Options:
    // 1. Simple alert (not recommended for UX)
    // 2. Toast notification (create a toast component)
    // 3. Inline message in UI

    console.log('SUCCESS:', message);
    // alert(message); // Temporary - replace with better UX
}

/**
 * Show error message to user
 * TODO: Implement error notification
 *
 * @param {string} message - Error message
 */
function showError(message) {
    // TODO: Implement error notification
    console.error('ERROR:', message);
    // alert(message); // Temporary - replace with better UX
}

/**
 * Refresh items on the page
 * TODO: Implement this to reload items from API and update DOM
 */
async function refreshItems() {
    // TODO: Implement refresh logic
    // const pantryItems = await loadItems('pantry');
    // const fridgeItems = await loadItems('fridge');
    //
    // renderItems('pantry', pantryItems);
    // renderItems('fridge', fridgeItems);
}

/**
 * Render items to the DOM
 * TODO: Implement this to dynamically create item cards
 *
 * @param {string} category - 'pantry' or 'fridge'
 * @param {Array} items - Array of item objects
 */
function renderItems(category, items) {
    // TODO: Implement rendering logic
    // const container = document.getElementById(`${category}-items`);
    //
    // if (items.length === 0) {
    //     container.innerHTML = `<p class="empty-state">No ${category} items yet. Add your first item!</p>`;
    //     return;
    // }
    //
    // container.innerHTML = items.map(item => createItemCardHTML(item)).join('');
}

/**
 * Create HTML for an item card
 * TODO: Implement this to match your item_card.html template
 *
 * @param {Object} item - Item object
 * @returns {string} HTML string
 */
function createItemCardHTML(item) {
    // TODO: Create HTML matching the template
    // return `
    //     <div class="item-card" data-item-id="${item.id}" data-status="${item.status}">
    //         ...
    //     </div>
    // `;
    return '';
}

// ============================================================================
// OPTIONAL ENHANCEMENTS
// ============================================================================

/**
 * Quick-add common items
 * TODO: Implement preset item names for faster adding
 */
function setItemName(name) {
    // TODO: Set item name in form
    // const nameInput = document.getElementById('item-name');
    // nameInput.value = name;
}

/**
 * Filter items by status
 * TODO: Implement filtering UI (show only plenty, running_low, or out)
 */
function filterByStatus(status, category) {
    // TODO: Implement filtering
}

/**
 * Search items by name
 * TODO: Add search functionality
 */
function searchItems(query) {
    // TODO: Implement search
}

// ============================================================================
// EXPORT (if using modules)
// ============================================================================

// If you decide to use ES6 modules, export your functions here
// export { loadItems, createItem, updateStatus, deleteItem, showShoppingList };
