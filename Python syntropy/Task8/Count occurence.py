def count_occurrences(element, *args):
    return args.count(element)

x = int(input("Enter the number of elements: "))
elements = []

print("Enter your elements:")
for i in range(x):
    e = input()
    elements.append(e)

target_element = input("Enter the element to count: ")

result = count_occurrences(target_element, *elements)
print(f"The number of occurrences of '{target_element}' is: {result}")
