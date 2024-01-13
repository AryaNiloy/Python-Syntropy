def sort_strings_by_length_arg(*args):
    return sorted(args, key=len)

x = int(input("Enter the number of strings: "))
strings = []

print("Enter your strings:")
for i in range(x):
    s = input()
    strings.append(s)

result = sort_strings_by_length_arg(*strings)
print(f"The sorted strings by length are: {result}")
   