
# Arithmetic operator
x = 4
y = 32
print((x+y)-x*y)
print(y/x+x/y)
#Logical operator
#and , or ,not
#Sequential Increament/Decreament
x = 7
x = x + 7
x += 7
x = x - 7  
x -= 7
x = x * 70
x *= 70
x = x / 70
x /= 10
x = x % 10
x %= 10
x = x / 3  
x =x// 3 #It eliminates fractions
print(x)
20
x = 20
y = 10
print(x is not y)#If the condition is true it will print true
# Condition
x = 2
if (not (x >= 10)):
   
    print("True")
else:
    print("False")
#multiple condition inside if
if (x > 10 or x == 10):
     print("True")
else:
    print("False")
         

x = "python"
print("P" in x)#if the character p is the string it will print true

basket = ['apple', 'orange', "$1000"]#list
print("pen" not in basket)

Syntax : [on_true] if [expression] else [on_false]

# if else sort form =>ternary operator

user_input = int(input("Enter a number: "))

result = "Positive" if user_input > 0 else "Non-positive"

# == and is
# 'is' is actually identity operator whereas == compares equality of objects
# is checks the address, it must be of the same otherwise will returnb false
# == checks the value inside variables
car = ['white', 10]
car1 = ['white', 10]

print(car[0] == car1[0])
print(car[0] is car[0])

#loop
#The for loop is used for iterating over a sequence (such as a list, tuple, string, etc.).
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#The while loop is used for executing a set of statements as long as a condition is true.
 # Printing numbers from 1 to 5 using a while loop
num = 1
while num <= 5:
    print(num)
    num += 1
#function
#define a function using the def keyword. 
def function_name(parameters):
    # code block
    # optional: return expression
#function_name: Name of the function.
#parameters: Input values that the function takes (optional).
#code block: The set of instructions to be executed when the function is called.
#return: Optional keyword to specify the value the function should return.

def greet():
    print("Hello, world!")
def add_numbers(a, b):
    sum_result = a + b
    return sum_result

# Calling the functions
greet()
result = add_numbers(3, 5)
print("The sum is:", result)   
