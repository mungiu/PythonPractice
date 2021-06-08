from math import ceil

print("This program prints a string 5 times")
for count in range(5):
    print("Python is cool")
for i in range(10):
    print(f"{i}: Andrei Mungiu 273473")

wish = input()
qty = input()
for q in range(int(qty)):
    print(f"{q}: I hereby grant your  wish: {wish}")


def is_even(my_number):
    return (my_number % 2) == 0


a = 0
while int(a) < 1:
    number = int(input())
    if number == 123:
        a = 1
        print("Bye for now!")
    if is_even(number):
        print(f"{number}")