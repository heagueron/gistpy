import string

def printstockprice(stock,price):
    for itemname in stock:
        itemprice = price[itemname]
        itemquantity = stock[itemname]
        print(str(itemname) + " " + str(itemquantity) + " " + str(itemprice))


def readstockprice(itemfilename, stock, price):
    # write your code here
    with open(itemfilename, 'r') as my_file:
        #lines = my_file.readlines()
        # print(lines) # ['banana 1 1.25\n', 'apple 6 1.75\n', 'orange 26 0.5\n', 'pear 55 2.5\n']
        for line in my_file:
            print(line)
            row = line.split(' ')
            stock[row[0]] = int(row[1])
            price[row[0]] = float(row[2])
        """
        rows = [ line.split(' ') for line in my_file.read().splitlines() ]
        for row in rows:
            stock[row[0]] = int(row[1])
            price[row[0]] = float(row[2])
        """
    return

def updatestockprice(itemfilename, stock, price):
    # write your code here
    with open(itemfilename, mode='wt', newline='') as my_file:
        for item, quantity in stock.items():
            print(f'{item} {quantity} {price[item]}', file=my_file )
    return

def readshoppinglist(shoppinglistfilename, shopping):
    # write your code here
    with open(shoppinglistfilename, newline='') as items:
        rows = [ line.split(' ') for line in items.read().splitlines() ]
        for row in rows:
            shopping[row[0]] = int(row[1])
    return



def process_order(shopping, stock, price):
    # write your code here
    total = 0
    for item, quantity in shopping.items():
        if stock[item] >= quantity:
            print(f'\nYou bought {quantity} {item}', )
            stock[item] = stock[item] - quantity
            total += price[item] * quantity
    print(f'\nCost of items sold is: {total}')
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
    print("\nafter reading: -------------------------------- ")
    printstockprice(stock, price)
    """
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
    print("\nafter updating: ------------------------------- ")
    printstockprice(stock, price)
    """
    
    return

if __name__ == "__main__":
    main()
