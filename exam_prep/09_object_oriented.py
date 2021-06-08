class MyRecipe:
    def __init__(self, calories, cookTime):
        self.calories = calories
        self.cookTime = cookTime

    def cook(self):
        print(f"Your food has {self.calories} calories and cook time in minutes is: {self.cookTime}")


rec1 = MyRecipe(100, 20)
rec2 = MyRecipe(200, 30)
rec3 = MyRecipe(300, 40)
rec4 = MyRecipe(400, 50)
rec5 = MyRecipe(500, 60)

rec1.cook()
rec2.cook()
rec3.cook()
rec4.cook()
rec5.cook()


class Contact:
    """ Exercise 9.2 """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


class AddressHolder:
    """ Exercise 9.2 """

    def __init__(self, street: str, post_code: int, city: str):
        self.street = street
        self.post_code = post_code
        self.city = city

    def __str__(self):
        return f"Street: {self.street}, Postal Code: {self.postal_code}, City: {self.city}"


class Friend(Contact, AddressHolder):
    """ Exercise 9.2 """

    def __init__(self, phone: str, name: str, email: str, street: str, post_code: int, city: str):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, post_code, city)
        self.phone = phone

    def __str__(self):
        return f"Phone: {self.phone} " \
               f"Name : {self.name} " \
               f"Email: {self.email} " \
               f"Street: {self.street} " \
               f"Post code: {str(self.post_code)} " \
               f"City: {self.city}"


friend = Friend("555555", "Andrei", "bro@gmail.com", "MyStreet", 23, "MyCity")
print(friend)


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

    def __init__(self, name: str, placeFound: str):
        self.name = name
        self.placeFound = placeFound

    def eat(self):
        print("The shark is eating...")

    def swim(self):
        print("The shark is swimming...")


class Dolphin(Fish):
    """ Exercise 9.4 """

    def __init__(self, name: str):
        self.name = name

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
