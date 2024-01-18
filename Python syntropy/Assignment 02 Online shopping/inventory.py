import json

def load_inventory():
    try:
        with open('inventory_data.json', 'r') as file:
            inventory_data = json.load(file)
    except FileNotFoundError:
        inventory_data = {}
    return inventory_data

def save_inventory(inventory_data):
    with open('inventory_data.json', 'w') as file:
        json.dump(inventory_data, file, indent=4)

def add_product(product_id, name, price, quantity, inventory_data):
    if product_id not in inventory_data:
        inventory_data[product_id] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        inventory_data[product_id]['quantity'] += quantity
    save_inventory(inventory_data)

def update_stock(product_id, quantity_change, inventory_data):
    if product_id in inventory_data and inventory_data[product_id]['quantity'] + quantity_change >= 0:
        inventory_data[product_id]['quantity'] += quantity_change
        save_inventory(inventory_data)
        return True
    return False
