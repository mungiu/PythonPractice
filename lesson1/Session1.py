import json

# CTRL + Enter executes
3 + 7
#
type(10)
#
type(4.)
#
x = 3.5
type(x)


#

# factorial formula n!  = n * (n-1)!, n > 0
# rec - used for telling F# that this is a recursive function
def factorial_recursive(x):
    if x < 1:
        return 1
    else:
        return x * factorial_recursive(x - 1)


while True:
    print(factorial_recursive(int(input("input factorial number: "))))


def main():
    num = int(input("Enter a positive integer: "))
    # check for validity
    fact = 1
    for factor in range(num, 1, -1):
        fact = fact * factor
    print("the factorial of {0:2} is: {1:2}".format(num, fact))
    # print("The factorial is :", fact, '\n')


main()

# converting dictionary to JSON
dtg_d1 = {"drink": "Coffee", "size": "Medium", "price": "25"}


json.dumps(dtg_d1)
