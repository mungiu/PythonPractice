from tkinter import *

# inpure function
G = 5  # global variable


def impure_sum(n):
    return n + G


print(impure_sum(5))


# pure function free from side effect
def pure_fun_sum(x, y):
    return x + y


def sumPositivesImp(list):
    for item in list:
        if item % 2 == 0:
            return item


print(pure_fun_sum(5, 5))


# returning lambda example
lambda_add = lambda x, y: x + y


pure_fun_sum(5, 5) == lambda_add(5, 5)
pure_fun_sum(5, 5) == (lambda x, y: x + y)(5, 5)
# Example of using lambda on the fly
(lambda x, y: x + y)(5, 5)

coffee_prices = [(100, 21), (101, 26), (103, 50)]
max(coffee_prices, key=lambda coffee_price: coffee_price[1])

tkwin = Tk()
tkwin.geometry('400x200')
btn = Button(tkwin, text='Interview result', command=(lambda: sys.stdout.write('Smile! You have been hired!')))
btn.pack()
mainloop()
