#EX 8.1
def firstPrint():
	for count in range(10):
		print("PepePls")

def secondPrint():
	i = 0
	while i < 10:
		print("NotLikeThis")
		i += 1

def thirdPrint(wish, qty):
	for count in range(qty):
		print(wish)

#def main():
#	firstPrint()
#	secondPrint()
#	thirdPrint(input("input wish: "), int(input("input wish quantity: ")))
#


#EX 8.2 - SUM LIST (imperative VS declarative)
numbers = [1, 2, 3, 4, 5, 6]
#imperative aprogramming – focuses on how to execute, defines control flow as statements that change a program state.
def sum_lst(lst):
	total = 0
	for number in lst:
		total += number
	return total
#declarative programming (functional) – focuses on what to execute, defines program logic, but not detailed control flow.
print(sum(numbers))									#using sum
import functools
print(functools.reduce(lambda x, y: x + y, numbers)) #using reduce


#EX 8.3 - check for even nnumbers (imperative VS declarative)
def printEvenInput():
	temp = int(input())
	if (temp % 2 == 0):
		print(temp)
	printEvenInput()
#def main():
#	printEvenInput()

#EX 8.4 - given a list and a groupLength, returns a list of lists with length groupLength.
def groupList(list, groupLength):
	count = 1;
	listOfLists = [];
	subList = [];
	for item in list:
		subList.append(item)
		if ((count % groupLength == 0)):
			listOfLists.append(subList.copy())
			subList = [];
		count += 1
	return listOfLists
#def main():
#	print(groupList(numbers, 2)) #[[1,2] [3,4] [5,6]]

#EX 8.5 - Create a dictionary specialle which stores software engineering specializations
dictionarySpecialle = { "Bob":"IoT", "Dora":"Media", "Paw":"Data" }
dictionarySpecialle["Bob"] = "Data"					# updating "Bob" value
dictionarySpecialle.update({"Farmer":"Climate"})	# inserts new item to dictionary
def main():
	print(dictionarySpecialle.get("Dora"))
	print(dictionarySpecialle.keys())
	print(dictionarySpecialle.get("Bob"))
main()