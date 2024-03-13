# Creating an empty tuple and printing it
tuple1 = ()
print(tuple1)

# Creating a tuple with integers and printing it
tuple2 = (1, 2, 3)
print(tuple2)

# Creating a tuple with mixed data types and printing it
tuple3 = (101, "Anirban", 20000.0, "HR Dept")
print(tuple3)

# Creating a tuple with nested elements and printing it
tuple4 = ("points", [1, 4, 3], (7, 8, 6))
print(tuple4)

# Creating a tuple without parentheses and printing it
tuple5 = 101, "Anirban", 20000.0, "HR Dept"
print(tuple5)

# Unpacking tuple elements and printing them individually
empid, empname, empsal, empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)

# Checking the type of a tuple
print(type(tuple5))

# Creating a tuple of characters and printing it
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)

# Accessing specific elements in a tuple
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])

# Creating a nested tuple and accessing its elements
nest_tuple2 = ("point", [1, 3, 4], (8, 7, 9))
print(nest_tuple2)
print(nest_tuple2[0][3])
print(nest_tuple2[1][2])
print(nest_tuple2[2][2])

# Slicing a tuple and printing the results
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])

# Attempting to modify a tuple (commented out due to error)
# tuple1[2] = 'x'

# Creating and printing a new tuple
tuple1 = ('g', 'o', 'o', 'd', 'b', 'y', 'e')
print(tuple1)

# Concatenating tuples and printing the result
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o''m', 'e')
print(tuple2)
print(tuple3)
print(tuple2 + tuple3)

# Repeating elements in a tuple and printing the result
print(("again",) * 4)

# Deleting elements in a tuple (commented out due to error)
# del tuple4[2]
del tuple4

# Printing the count and index of specific elements in a tuple
tuple5 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple5.count('e'))
print(tuple5.index('c'))

# Iterating through a tuple and printing each element
tuple6 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
for letters in tuple6:
    print("letter is -> ", letters)

# Finding maximum, minimum, and length of a tuple and sorting its elements
tuple7 = (22, 33, 55, 44, 77, 66, 11)
print(tuple7)
print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))
