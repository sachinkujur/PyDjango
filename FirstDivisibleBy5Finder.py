# Example 1: Printing the first number divisible by 5 from a list, or "not found" if none is found
nums_1 = [12, 15, 18, 21, 26]

# Iterate through each number in nums_1
for num in nums_1:
    # Check if the number is divisible by 5
    if num % 5 == 0:
        # Print the first divisible number and exit the loop
        print(num)
        break
else:
    # If the loop completes without a break, print "not found"
    print("not found")

# Example 2: Printing the first number divisible by 5 from a list, or "not found" only once
nums_2 = [23, 24, 27, 38, 29]

# Initialize a flag to track whether a divisible number is found
found = False

# Iterate through each number in nums_2
for num in nums_2:
    # Check if the number is divisible by 5
    if num % 5 == 0:
        # Print the first divisible number, set the flag to True, and exit the loop
        print(num)
        found = True
        break

# If no divisible number is found, print "not found"
if not found:
    print("not found")
