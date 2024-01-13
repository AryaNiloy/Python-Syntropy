def concatenate_strings(*args):
    return ''.join(args)

x = int(input("Enter the number of strings: "))
strings = []

print("Enter your strings:")
for i in range(x):
    s = input()
    strings.append(s)

result = concatenate_strings(*strings)
print(f"The concatenated string is: {result}")