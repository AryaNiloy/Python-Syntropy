def avg_arg(*args):
    return sum(args)/len(args)

x = int(input("Enter the number of arguments: "))
arguments = []

print("Enter your arguments:")
for i in range(x):
    y = int(input())
    arguments.append(y)

result = avg_arg(*arguments)
print(f"The average of the arguments is: {result}")
