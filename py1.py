#to check python version on editor
import sys
print(sys.version)

if (5>2):
    print("5 is greater than",2)
    
#this is a comment
        
print("line", end = " ") # it doesnt change line after printing the text.
print("same line")

"""
MULTIPLE LINE COMMENT
MULTIPLE LINE COMMENT

"""

a = 4
print(a)
a = "four"
print(a)

#casting
print("casting")
x =int(4)

print(x)
x =float(4)
print(x)

#datatype
print(type(x))

x, y, z = 2, 3, "string"
print(x, y, z)

x=y=z = "oranges"
print(x, y, z)

#unpacking list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x=complex(4,5)
print(x)

