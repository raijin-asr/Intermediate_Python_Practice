# create the Engine class
class Engine:
    # use __init__() to initialize the power attribute 
    def __init__(self, power):
        self.power= power

# create the Vehicle class
class Vehicle:
    # use __init__() to initialize the wheels attribute
 
    def __init__(self, wheels):
        self.wheels = wheels
        
        # the engine attribute should be an object of the Engine class with the power attribute 400
        self.engine = Engine(400)
    
    # create the get_power() method
    def get_power(self):
        # print the power attribute of the engine attribute (which is an object of Engine) 
        print(self.engine.power)

# create an object of Vehicle
v1= Vehicle(4)

# call the get_power() method using the object
v1.get_power()