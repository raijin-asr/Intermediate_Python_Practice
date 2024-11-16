# create the Animal class
class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("I can eat food")

# create the Dog class
class Dog(Animal): #inherit the Animal class
    def __init__(self):
        pass

    def bark(self):
        print("I can bark")

# create an object of Dog
d1= Dog()

# call the eat() method using the object
d1.eat()