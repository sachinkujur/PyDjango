class MyComplexNumber:
    def __init__(self, real=0, imag=0):
        # Constructor to initialize the complex number with real and imaginary parts
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.imag_part = imag

    def displayComplex(self):
        # Method to display the complex number
        print("{0} + {1}j".format(self.real_part, self.imag_part))


# Creating an instance of the MyComplexNumber class with real and imaginary values
cmplx1 = MyComplexNumber(40, 50)

# Calling the displayComplex method to print the complex number
cmplx1.displayComplex()

# Creating another instance of the MyComplexNumber class
cmplx2 = MyComplexNumber(60, 70)

# Adding a new attribute to the second instance
cmplx2.new_attribute = 80

# Calling the displayComplex method for the second instance
cmplx2.displayComplex()

# Printing the values of real_part, imag_part, and the new_attribute for the second instance
print((cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute))

# Printing the representation of cmplx1 (default implementation of __str__ method)
print(cmplx1)

# Deleting the real_part attribute of cmplx1
del cmplx1.real_part

# Deleting the entire instance cmplx1
del cmplx1

# Attempting to print cmplx1 after deletion will result in an error
print(cmplx1)  # This line will raise an error since cmplx1 is deleted
