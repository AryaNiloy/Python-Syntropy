def add_to_cart(product_id, quantity, cart_data, inventory_data):
    if product_id in inventory_data and inventory_data[product_id]['quantity'] >= quantity:
        if product_id not in cart_data:
            cart_data[product_id] = {'name': inventory_data[product_id]['name'], 'price': inventory_data[product_id]['price'], 'quantity': quantity}
        else:
            cart_data[product_id]['quantity'] += quantity
        return True
    return False

def view_cart(cart_data, inventory_data):
    total_amount = 0
    for product_id, details in cart_data.items():
        name = details['name']
        price = details['price']
        quantity = details['quantity']
        total_amount += price * quantity
        print(f"Product: {name}, Quantity: {quantity}, Price: {price}, Subtotal: {price * quantity}")
    print(f"Total Amount: {total_amount}")
