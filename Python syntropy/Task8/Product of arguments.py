def product_arg(*args):
    result = 1
    for num in args:
        result *= num
    return result

x = int(input("Enter the number of arguments: "))
arguments = []

print("Enter your arguments:")
for i in range(x):
    y = int(input())
    arguments.append(y)

result = product_arg(*arguments)
print(f"The product of the arguments is: {result}")