class PythonClassExample(object):
    """description of class"""

    # in this case every time we initialize the class we will print
    # since that is what we wrote inside the constructor
    def __init__(self, name):
        self.name = name
        print(self.name)


p1 = PythonClassExample("Andrei Mungiu")


# In the below class the base class is also "object" but it is implicit
# Everything in python is an objects
# The "object" has its own definition of "__init__" which is used as a
# constructor
# if we do not defined a constructor for our class explicitly
# class PythonClassExample:
#   pass
class ViaStudent:
    # FORM definition start
    where = "VIA"

    # FORM definition END
    def __init__(self):
        self.where = "VIA-Horsens"


print(ViaStudent.where)  # prints "VIA"
print(ViaStudent().where)  # prints "VIA-Horsens"


class Vehicle(object):
    def __init__(self, number_of_tires):
        self.__numberOfTires = number_of_tires

    @property
    def number_of_tires(self):
        print("Number of tires is: ", self.__numberOfTires)
        return self.__numberOfTires

    @number_of_tires.setter
    def number_of_tires(self, value):
        print("Setting number of tires to: ", value)
        self.__numberOfTires = value

    @property
    def description(self):
        return "Description. Tire Nr.: ", self.__numberOfTires


# extending the Vehicle class
class Car(Vehicle):
    def __init__(self, plate_number, number_of_tires):
        self.__plateNumber = plate_number
        super().__init__(number_of_tires)

    @property
    def license_plate(self):
        print("License plate is: ", self.__plateNumber)
        return self.__plateNumber

    @license_plate.setter
    def license_plate(self, value):
        print("Setting license plate to: ", value)
        self.__plateNumber = value


# extending the Vehicle class
class Motorcycle(Vehicle):
    def __init__(self, plate_number, number_of_tires):
        self.__plateNumber = plate_number
        super().__init__(number_of_tires)

    @property
    def license_plate(self):
        print("License plate is: ", self.__plateNumber)
        return self.__plateNumber

    @license_plate.setter
    def license_plate(self, value):
        print("Setting license plate to: ", value)
        self.__plateNumber = value


myTesla = Car("MyPlateNumber", 4)

print("Outer print: ", myTesla.description)
print("Outer print: ", myTesla.license_plate)
print("Outer print: ", myTesla.number_of_tires)
