def reverse_list_arg(*args):
    return list(args)[::-1]

x = int(input("Enter the number of elements in the list: "))
elements = []

print("Enter your elements:")
for i in range(x):
    element = input()
    elements.append(element)

result = reverse_list_arg(*elements)
print(f"The reversed list is: {result}")
