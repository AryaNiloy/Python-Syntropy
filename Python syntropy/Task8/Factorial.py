def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)
    
x=input("Enter a  number to find factorial: ") 
y= calculate_factorial(x)
print(y)