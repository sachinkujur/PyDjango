# Define a Person class with default attributes.
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10

    # Method to display information about the person.
    def info(self):
        print(f"{self.name} is a {self.occupation}")

# Create instances of the Person class.
a = Person()
b = Person()
c = Person()

# Modify attributes for each instance.
a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# Display information for specific instances.
a.info()  # Output: Shubham is an Accountant
b.info()  # Output: Nitika is an HR
