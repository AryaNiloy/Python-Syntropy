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

