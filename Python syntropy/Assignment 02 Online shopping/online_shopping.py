from inventory import load_inventory, save_inventory, add_product, update_stock
from shopping_cart import add_to_cart, view_cart
from payment import process_payment

def main():
    inventory_data = load_inventory()
    cart_data = {}

    while True:
        print("1. View Inventory")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Inventory:")
            for product_id, details in inventory_data.items():
                print(f"Product ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Quantity: {details['quantity']}")

        elif choice == '2':
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity: "))
            if add_to_cart(product_id, quantity, cart_data, inventory_data):
                print("Product added to cart successfully.")
            else:
                print("Invalid product ID or insufficient stock.")

        elif choice == '3':
            print("Shopping Cart:")
            view_cart(cart_data, inventory_data)

        elif choice == '4':
            print("Checkout:")
            view_cart(cart_data, inventory_data)
            total_amount = sum(details['price'] * details['quantity'] for details in cart_data.values())
            process_payment(total_amount)
            for product_id, details in cart_data.items():
                update_stock(product_id, -details['quantity'], inventory_data)
            cart_data = {}
            save_inventory(inventory_data)
            print("Checkout completed successfully.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
