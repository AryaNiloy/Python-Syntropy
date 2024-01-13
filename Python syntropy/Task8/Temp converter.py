def cel_to_far(*temp):
    return [(c * 9/5) + 32 for c in temp]
x=input("Enter temperature in celsius to convert into farenheit ")
cel_to_far(x)
print(x)