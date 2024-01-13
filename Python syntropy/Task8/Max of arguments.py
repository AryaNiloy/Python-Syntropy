def max_arg(*args):
    return max(args)

x = int(input("Enter the number of arguments: "))
arguments = []

print("Enter your arguments:")
for i in range(x):
    y = int(input())
    arguments.append(y)

result = max_arg(*arguments)
print(f"The maximum number in the arguments is: {result}")
