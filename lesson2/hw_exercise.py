class MyRecipe:
    """ Exercise 9.1 """

    def __init__(self, calories, cook_time):
        self.calories = calories
        self.cook_time = cook_time

    def cook(self):
        print(f"Cook time is: {self.cook_time} minutes, and it will contain {self.calories} calories")


recipeTest = MyRecipe(500, 1)


class Contact:
    """ Exercise 9.2 """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


class AddressHolder:
    """ Exercise 9.2 """

    def __init__(self, street, post_code, city):
        self.street = street
        self.post_code = post_code
        self.city = city

    def __str__(self):
        return f"Sreet: {self.street}, Postal Code: {self.postal_code}, City: {self.city}"


class Friend(Contact, AddressHolder):
    """ Exercise 9.2 """

    def __init__(self, name, email, street, post_code, city, phone):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, post_code, city)
        self.phone = phone


testFriend = Friend("Valeria", "vm@vm.com", "TheStreet", "PO8000", "City")
print(testFriend.__str__())


class Fish:
    """ Exercise 9.3 """

    @staticmethod
    def eat():
        print("The fish eats...")

    @staticmethod
    def swim():
        print("The fish swims...")


class Shark(Fish):
    """ Exercise 9.3 """

    def __init__(self, name, place_found):
        self.name = name
        self.place_found = place_found
        Fish.__init__(self)

    def eat(self):
        print("The shark is eating...")

    def swim(self):
        print("The shark is swimming...")


class Dolphin(Fish):
    """ Exercise 9.3 """

    def __init__(self, name):
        self.name = name
        Fish.__init__(self)

    def eat(self):
        print("The dolphin is eating...")

    def swim(self):
        print("The dolphin is swimming...")


testDolphin = Dolphin("Valeria")
testShark = Shark("Andrei", "Home")
testFish = Fish()

testDolphin.eat()
testDolphin.swim()
testShark.eat()
testShark.swim()

testFish.eat()
Fish.swim()
