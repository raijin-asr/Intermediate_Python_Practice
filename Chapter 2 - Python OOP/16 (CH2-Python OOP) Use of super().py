# create the Animal class
class Animal:
    def __init__(self):
        pass
    
    def eat(self):
        print("I can eat food")

# create the Dog class
class Dog(Animal):
    def __init__(self):
        super().__init__() # call the __init__() method of the base class

    def bark(self):
        print("I can bark")

# create an object of the Dog class
d1 = Dog()

# call the eat() method using the object
d1.eat()