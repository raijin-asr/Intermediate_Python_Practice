# create the class
class Square:

    # define the __init__() method
    def __init__(self, length):
        self.length= length
  
    # define the compute_area() method
    def compute_area(self):
        return (self.length *self.length)
    
    # define the compute_perimeter() method
    def compute_perimeter(self):
        return (4 * self.length)


# get integer input
length = int(input())

# create an object of Square    
s1= Square(length)

# call compute_area() and print the area
print(s1.compute_area())

# call compute_perimeter() and print the perimeter
print(s1.compute_perimeter())