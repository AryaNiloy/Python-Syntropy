inven = ["Bike", "Glass", "Phone", "Key"]
inv_qua = [400, 788, 988, 624]
price = [100000, 1000, 45000, 20]
cart = []
def view_inv():
    for item in inven:
        print(item)
def add_item():
    n = int(input("How many items you want to add? "))
    for i in range(1, n + 1):
        print("Enter the item name, quantity, and price you want to add ")
        it = input()
        qu = int(input())
        pr = int(input())
        inven.append(it)
        inv_qua.append(qu)
        price.append(pr)
    print("The above items have been added successfully")
def rem_item():
    n = int(input("How many items you want to remove? "))
    for i in range(1, n + 1):
        print("Enter the item name and quantity you want to remove ")
        it = input()
        qu = int(input())
        if it in inven and qu in inv_qua:
            index = inven.index(it)
            inven.pop(index)
            inv_qua.pop(index)
            price.pop(index)
            print(f"{it} removed successfully.")
        else:
            print(f"{it} not found in the inventory or quantity does not match.")
def add_cart():
    item_name = input("Enter item name to add to cart: ")
    if item_name in inven:
        index = inven.index(item_name)
        if inv_qua[index] > 0:
            cart.append(item_name)
            print(f"{item_name} added to the cart.")
        else:
            print(f"Sorry, {item_name} is out of stock.")
    else:
        print(f"{item_name} not found in the inventory.")
def view_cart():
    print("Cart:")
    for item in cart:
        print(item)
def checkout():
    total_price = sum([price[inven.index(item)] for item in cart])
    print(f"Total price is {total_price}")
def exit_program():
    print(f"Nice business with you {z} , take care" )
z=input("Enter your name sir/madam ")
y=input("Enter contact please ")
while True:
    print("\nOptions:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Checkout")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_inv()
    elif choice == 2:
        add_item()
    elif choice == 3:
        rem_item()
    elif choice == 4:
        add_cart()
    elif choice == 5:
        view_cart()
    elif choice == 6:
        checkout()
    elif choice == 7:
        exit_program()
        break
    else:
        print("Invalid choice. Please try again.")