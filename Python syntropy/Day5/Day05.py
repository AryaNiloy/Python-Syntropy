#What is list?
#An ordered sequence of vaieties of data
my_list = ["Ball",100,"Computer","Python","C",]
my_list
print(type(my_list))
print(my_list[2]) # We can access any item with the help of index
#Index begins from 0 not 1
#acces the last item
print(my_list[-1])
#Select items from a definite range
print(my_list[0:2]) #[a:b] It selects items from a to b-1
#Data type of a particular item inside list
print(type(my_list[1]))
#Accessing from the end
print(my_list[-3])
print(my_list[-3:])
#loop in list
for i in my_list:
     print(i)
#List modification
my_list.append("Laptop")#Adds an item at the end
print(my_list)
my_list.insert(2,200)#Adds an item to the specified index
print(my_list)
my_list.remove(200)
print(my_list)
my_list.pop()#Removes last item
print(my_list)
#List membership
100 in my_list
if 100 in my_list:
    print("IN")
else:
    print("NOT IN") 
#REverse and sorting    
list1=[10,2,305,4.3,55]
list1.reverse()
print(list1)
list1[::-1]
print(list1)
list1.sort(reverse=True)
print(list1)
sorted(list1)
print(list1)
#string to list
name="Mymensingh"
list2=[i for i in name ]
print(list2)
#All/any
list3=["horse","death",False]
print(all(list3))
print(any(list3))
#Frequency 
list4=["Cat","Bat","Rat","Cat","Bat","Hat"]
list4.count("Bat")