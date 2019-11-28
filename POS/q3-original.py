import string

def printstockprice(stock,price):
    for itemname in stock:
        itemprice = price[itemname]
        itemquantity = stock[itemname]
        print(str(itemname) + " " + str(itemquantity) + " " + str(itemprice))


def readstockprice(itemfilename, stock, price):
    # write your code here
    with open('itemfilename', newline='\\') as fruits:
        rows = [ line.split('\\') for line in fruits.read().splitlines() ]
        print(rows)

    #######
    return

def updatestockprice(itemfilename, stock, price):
    # write your code here
    return

def readshoppinglist(shoppinglistfilename, shopping):
    # write your code here
    return



def process_order(shopping, stock, price):
    # write your code here
    return


# YOU HAVE TO SUBMIT YOUR CODE WITH FOLLOWING LINES WITHOUT ANY MODIFICATION
# You may play with the following code, by commenting out lines of code as you gradually develop your solution

def main():

    # reading filenames from user
    # first file should have items stock & price
    # second file should have shopping list
    filenameinput = input("Enter filenames: ")
    filenames = filenameinput.split();
    itemsfilename = filenames[0]
    shoppinglistfilename = filenames[1]

    # dictionary variables
    stock = {}
    price = {}
    shopping = {}

    # reading stock & price from file
    readstockprice(itemsfilename, stock, price)

    # displaying stock & price after reading
    # print("\nafter reading: -------------------------------- ")
    # printstockprice(stock, price)

    # reading shopping list
    readshoppinglist(shoppinglistfilename,shopping)

    # processing order and printing sale detail
    print("\nprocessing order.. POS print:------------------- ")
    process_order(shopping, stock, price)

    # displaying stock & price after sale
    print("\nafter sale:------------------------------------- ")
    printstockprice(stock, price)

    # update stock & price after sale
    updatestockprice(itemsfilename, stock, price)

    # displaying stock & price after update
    # print("\nafter updating: ------------------------------- ")
    # printstockprice(stock, price)


    return

if __name__ == "__main__":
    main()
