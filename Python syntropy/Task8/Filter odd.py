def filter_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False
x = int(input("Enter the number of arguments: "))
arguments = []
print("Enter your arguments:")
for i in range(x):
    y = int(input())
    arguments.append(y)
result = list(filter(filter_odd, arguments))
print(f"The list of the even numbers is: {result}")
