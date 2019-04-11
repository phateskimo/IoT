# Week 3 assignment
# by Chris Larson

conf = "you entered- "
print ("we're going to ask you for 3 different numbers, then we're going to do some magic computer stuff")
firstString = input("Please enter a number: ")
print (conf + firstString)
first = int(firstString)
secondString = input("would you kindly enter another number?: ")
print (conf + secondString)
second = int(secondString)

print("I know this is getting a little old but would you humor us just one more time?")
thirdString = input("please enter a third number for us: ")
print (conf + thirdString)
third = int(thirdString)

print("thank you, now for some magic")

list = [first,second,third]

print("you entered the following numbers: " + str(list))

list.sort()

print("but the assignment calls for sorting the numbers, so let's sort that list.")
print("in numerical order, the numbers you entered are: " + str(list))

print("another way to look at the list is like this:")
for entry in list:
    print(entry)

               
