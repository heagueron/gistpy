# list comprehension

def SmartSquare(inlist, inplace):
    if inplace == True:
        for index,x in enumerate(inlist):
            inlist[index] = x*x
        return inlist
    return [x*x for x in inlist]


# DO NOT CHANGE CODE BELOW
mylist = []
n = int (input("Enter number of elements in the List : "))
for i in range(0, n):
    num = int(input("Num "+str(i+1)))
    mylist.append(num)

print(mylist, SmartSquare(mylist, False))
print(mylist, SmartSquare(mylist, True))
mylist = []
n = int (input("Enter number of elements in the List : "))
for i in range(0, n):
    num = int(input("Num "+str(i+1)))
    mylist.append(num)

print(mylist, SmartSquare(mylist, False))
print(mylist, SmartSquare(mylist, True))
