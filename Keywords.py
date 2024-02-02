# Importing the math module and aliasing it as myMath
import math as myMath

# Printing the cosine of pi using the math module
print(myMath.cos(myMath.pi))

# Comparisons and logical operations
print(5 == 5)
print(5 > 5)

# None comparisons
print(None == 0)
print(None == False)
print(None == [])
print(None == None)


# Defining a void function and calling it
def a_void_function():
    a = 1
    b = 2
    c = a + b


x = a_void_function()  # calling the void function and printing the result, which is None

# Logical operations
print(True and False)
print(True or False)
print(not False)
print(True and True)
print(True or True)
print(not True)

# Assertions
assert 5 > 4
assert 5 == 5

# Looping with break and continue
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for i in range(1, 8):
    if i == 5:
        continue
    print(i)


# Class definition and method calling
class ExampleClass:
    def function1(parameters):
        print("function1() executing...")

    def function2(parameters):
        print("function2() executing...")


ob1 = ExampleClass()
ob1.function1()
ob1.function2()


# Function definition with pass
def function_name(parameters):
    pass


function_name(10)

# Variable scope and deletion
a = 10
print(a)
del a
# print(a)  # Uncommenting this line would raise an error since 'a' is deleted

# Conditional statements
num = 4
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")

# Exception handling
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Execution Successfully")

# Looping with a range
for i in range(1, 10, 1):
    print(i)

# Importing a specific function from the math module
from math import cos

print(cos(10))

# Global variable
globalvar = 10


# Functions to read and modify the global variable
def read1():
    print(globalvar)


def write1():
    global globalvar
    globalvar = 5


def write2():
    globalvar = 15  # This creates a new local variable instead of modifying the global one


read1()
write1()
read1()
write2()
read1()

# Membership operators
a = [1, 2, 3, 4]
print(4 not in a)
print(44 not in a)

# Identity operator
print(True is True)

# Lambda function
a = lambda x: x * 2
for i in range(1, 6):
    print(i, a(i))


# Nested functions with nonlocal keyword
def outer_function():
    a = 5

    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ", a)

    inner_function()
    print("Outer function: ", a)


outer_function()


# Function definition with pass
def function(args):
    pass


function(10)


# Function returning a value
def func_return():
    a = 10
    return a


print(func_return())

# While loop
i = 5
while i > 0:
    print(i)
    i -= 1

# Writing to a file using the 'with' statement
with open("example.txt", "w") as my_file:
    my_file.write("Hello World!")


# Generator function
def generator():
    for i in range(6):
        yield i * i


# Creating a generator object and iterating over it
g = generator()
for i in g:
    print(i)
