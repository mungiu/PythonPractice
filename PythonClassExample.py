class PythonClassExample(object):
    """description of class"""
    # in this case every time we initialize the class we will print
    # since that is what we wrote inside the constructor
    def __init__(self, name):
        self.name = name
        print(self.name)
    
p1 = PythonClassExample("Andrei Mungiu")

## In the below class the base class is also "object" but it is implicit
## Everything in python is an objectss
## The "object" has its own definition of "__init__" which is used as a constructor
## if we do not defined a constructor for our class explicitly
#class PythonClassExample:
#   pass

class ViaStudent:
    ## FORM definition start
    where = "VIA"
    ## FORM definition END
    def __init__(self):
        self.where = "VIA-Horsens"

print(ViaStudent.where)     # prints "VIA"
print(ViaStudent().where)   # prints "VIA-Horsens"

class Vehicle(object):
    def __init__(self, numberOfTires):
        self.__numberOfTires = numberOfTires

    @property
    def numberOfTires(self):
        print("Number of tires is: ", self.__numberOfTires)
        return self.__numberOfTires

    @numberOfTires.setter
    def numberOfTires(self, value):
        print("Setting number of tires to: ", value)
        self.__numberOfTires = value

    @property
    def description(self):
        return "Description. Tire Nr.: ", self.__numberOfTires

#extending the Vehicle class
class Car(Vehicle):
    def __init__(self, plateNumber, numberOfTires):
        self.__plateNumber = plateNumber
        super().__init__(numberOfTires)

    @property
    def licensePlate(self):
        print("License plate is: ", self.__plateNumber)
        return self.__plateNumber

    @licensePlate.setter
    def licensePlate(self, value):
        print("Setting license plate to: ", value)
        self.__plateNumber = value

#extending the Vehicle class
class Morotcycle(Vehicle):
    def __init__(self, plateNumber, numberOfTires):
        self.__plateNumber = plateNumber
        super().__init__(numberOfTires)

    @property
    def licensePlate(self):
        print("License plate is: ", self.__plateNumber)
        return self.__plateNumber

    @licensePlate.setter
    def licensePlate(self, value):
        print("Setting license plate to: ", value)
        self.__plateNumber = value

myTesla = Car("MyPlateNumber", 4)

print("Outer print: ", myTesla.description)
print("Outer print: ", myTesla.licensePlate)
print("Outer print: ", myTesla.numberOfTires)