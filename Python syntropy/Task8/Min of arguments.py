def min_arg(*args):
    return min(args)

x = int(input("Enter the number of arguments: "))
arguments = []

print("Enter your arguments:")
for i in range(x):
    y = int(input())
    arguments.append(y)

result = min_arg(*arguments)
print(f"The minimum number in the arguments is: {result}")