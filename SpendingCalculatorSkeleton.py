'''
Created on Oct 19, 2017

@author: Jocelyn Chen
'''
# import module
import sys

################  Global Variables  ##################
# TODO: 
# Declare a Grocery_List variable which should keep all the grocery information
# The Grocery_List should contain item, and its price 
Grocery_List = []

# boolean to maintain the for loop for the main
run = True

# Helper functions
######## Input for Int or Float ################
def cast_int(arg):
    try:
        return int(arg)
    except ValueError:
        print("Please make sure you enter an integer")
        return ValueError
    
def cast_float(arg):
    try:
        return float(arg)
    except ValueError:
        print("Please make sure you enter an float")
        return ValueError
if value error = False
print "Not a substancial number"
Break:
def make_sure_type_input(prompt, tyype):
    type_map = {
        'Integer': cast_int,
        'Float': cast_float
    }
    while(True):
        user_input = input(prompt)
        res = type_map[type](user_input)
        if(res != ValueError): 
            return res

############################################

# Print Grocery List
def printList():
    print("Current Grocery List:")
    print("TODO: Print all item in Grocery List here, including item name, price and quantity")
    # TODO: Print all item in Grocery List here
        for i in Grocery_List:
            print(i[0] + "/t" i[1] + "/t" i[2]+ "/t" i[3]+ "/t" i[3]+ "/t" i[4]+ "/t" i[5])

# Insert an Item to the Grocery List
def insertItem():
    print("Insert an item to the grocery list")
    print("TODO: ask user to insert item name, price, and quantity, and add the results to the grocery list")
    # TODO: ask user to insert item name, price, and quantity, and add the results to the grocery list
    # HINT 1: make use of the make_sure_type_input() function when ask user to enter a number
      return make_sure_type_input("Choose from 1 to 6: ", "Integer")

    # HINT 2: you should insert into the grocery list using the function append()
    
# Delete Grocery List
def deleteItem():
    print("Delete an item from the grocery list")
    item_name = input("Enter the exact item name you want to delete: ")
    for i in range(len(Grocery_List)):
        item = Grocery_List[i]
        if(item[0] == item_name):
            Grocery_List.pop(i)
            break;
    print("The item name you entered is not in the list!")
    
# Clear Grocery List
def clearItem():
    print("Clear list")
    print("TODO: Implement the function that empty the grocery list")
    # TODO: Implement the function that empty the grocery list
    
# Calculate the output
def calculate():
    print("Calculate the total cost for your shopping plan...")
    print("TODO: Implemenet code to calculate the total price for the grocery list")
    # TODO: Calculate the total price
    print 
    print("Happy Shopping! :)")

def processInput(option):
    if (option == 1):
        printList()
    elif (option == 2):
        insertItem()
    elif (option == 3):
        deleteItem()
    elif (option == 4):
        clearItem()
    elif (option == 5):
        calculate()
    elif (option == 6):
        # This is the quit option, we quit the program
        print("Quitting the program...")
        sys.exit(0)

# Get user input
def getInput():
    return make_sure_type_input("Choose from 1 to 6: ", "Integer")

# Show menu to users
def showMenu():
    print("Choose from the following options:")
    print("1. Show the current grocery list")
        for i in 
    print(i[0] + "/t" i[1] + "/t" i[2])

    print("2. Add a new item to the list")
Grocery_list.append(item+price)

    print("3. Remove an item from the list")
    print("4. Clear the list")
    print("5. Calculate the shopping list")
    print("6. Quit")

if __name__ == '__main__':
    # Main Menu
    print("Welcome to the spending calculator!")
    while(run):
        showMenu()
        processInput(getInput())
print (Grocery_List)