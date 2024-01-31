# Print the original array
arr = [10, 20, 30, 40, 50]
print(arr)

# Access individual elements of the array
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

# Print a list of brands
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

# Get the number of brands
num_brands = len(brands)
print(num_brands)

# Append a new brand to the list
brands.append("Intel")
print(brands)

# Print a list of colors
colors = ["voilet", "indigo", "blue", "green", "yellow", "orange", "red"]
print(colors)

# Delete an element at index 4
del colors[4]
print(colors)

# Remove the element "blue" from the list
colors.remove("blue")
print(colors)

# Pop the element at index 3
colors.pop(3)
print(colors)

# Print a list of fruits
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

# Modify elements in the list
fruits[1] = "Pineapple"
print(fruits)

# Update the last element in the list
fruits[-1] = "Guava"
print(fruits)

# Concatenate two lists
concat = [1, 2, 3]
print(concat)

# Concatenate a list with another list using "+"
concat + [4, 5, 6]
print(concat)

# Update the concatenated list
concat = concat + [4, 5, 6]
print(concat)

# Repeat elements in a list
repeat = ["a"]
print(repeat)

# Repeat the list elements 5 times
repeat = repeat * 5
print(repeat)

# Slicing operations on a list of fruits
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[: 3])
print(fruits[-4:])
print(fruits[-3:-1])

# Multi-dimensional list
multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
