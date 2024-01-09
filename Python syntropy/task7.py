#Tuple
#tuple is a collection of varities of data which is ordered and unchangeable
tup1=("Car",100,"Bike")
print(type(tup1))
print(tup1)
#index
print(tup1[0:2])
print(tup1.index(100))
print(type(tup1[1]))
#loop
for i in enumerate(tup1):
    print(i)
for i in tup1:
    print(i)    
mytuple1=('one','two','three','four','one','one','two','three')
print("Number of one is",mytuple1.count('one'))
'one' in mytuple1
print(len(mytuple1))
#tuple from string
hello=tuple("Hello")
print(hello)
#string
hi="Hi instructor"
print(type(hi))
word1="Hi"
word2="instructor"
print(word1 +     word2)
print(len(word1+word2))
#slicing string
print(hi[0:3])
learn="I am learning python online"
vowel=["A","I","E","O","U","a","e","i","o","u"]
temp=0
def vcount(learn):
       print("Vowels in the string ",learn.count("A")+learn.          count("E")+learn.count("I")+learn.count("O")+learn.count("U")+learn.count("a")+  learn.count("e")+learn.count("i")+learn.count("o")+learn.count("u"))
vcount(learn)
#stringsplit
my_phrase = "I am learning python online"
my_words = my_phrase.split()
for word in my_words:
    print(word)
#upperlower
print(hi.upper())
#checkfordigit
word = '32'
print(word.isdigit())
#Looping Constructs:
#for and while loops iterate over sequences or conditions.
#Example: 
my_list=[100,30]
for item in my_list: print(item)
#Function Creation and Usage:
#Functions encapsulate reusable code.
#Example:
def add_numbers(a, b):
    return a + b
result = add_numbers(2, 3)
#Module Importing and Utilization:
#Importing external modules extends functionality.
#Example: 
import math 
result = math.sqrt(16)
#Conditional Statements:
#if, elif, and else control program flow.
#Example
x=20
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
#Error Handling:
#try, except, finally handle exceptions.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
#File Input and Output Handling:
#Reading/writing data to/from files.
with open('file.txt', 'r') as file:
    content = file.read()
#Data Structures (Dictionary, Sets):
#Dictionaries store key-value pairs, sets store unique elements.
my_dict = {'name': 'John', 'age': 25}
my_set = {1, 2, 3, 3}
#Recursion Implementation:
#A function calls itself.
#Example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Functional Programming with Lists:
#Functions are first-class citizens; operations can be applied to lists.
#Example:
squared_numbers = list(map(lambda x: x**2, my_list))
#Concurrency and Multithreading:
#Executing multiple tasks concurrently.
import threading
import time
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Introducing a delay of 1 second
        print(f"Thread: {threading.current_thread().name}, Number: {i}")

thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_numbers, name="Thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Main thread exiting.")
#API Interaction:
#Interacting with external APIs for data exchange.
import requests
response = requests.get('https://api.example.com/data')
#Web Scraping:
#Extracting information from websites.
#Data Visualization:
#Representing data graphically.
#Unit Testing:
#Ensuring individual units of code work as expected.
#Asynchronous Programming:
#Executing tasks concurrently without blocking.
#Machine Learning/Deep Learning (Optional):
#Using models to make predictions or classify data
#Database Interaction:
#Connecting to and manipulating databases.