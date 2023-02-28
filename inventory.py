# importing tabulate module so we can display data in the table
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    # Initialising class Shoe with attributes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # function that returns the cost of the Shoe object
    def get_cost(self):
        return self.cost
    # function that returns quantity of the shoes
    def get_quantity(self):
       return self.quantity
    # function that returns string representation of the Shoe object 
    def __str__(self):
        return "{},{},{},{},{}".format(self.country, self.code, self.product, self.cost, self.quantity)


#=============Shoe list===========
# The list that will store Shoe objects
shoe_list = []
#==========Functions outside the class=============
 # function that opens inventory.txt file
def read_shoes_data():
    try:# openning and reading text file 
        inventory = open("inventory.txt","r")
        inventory_read = inventory.readlines()
        #using enumerate method so we can have access to index in order to skip reading first line of text file
        for i, line in enumerate(inventory_read):
            if i == 0:  # skip first line
                continue
            split = line.strip('\n').split(",")
            #handling error in case there is less then 5 peaces of data on 1 text line
            if len(split) < 5:
                raise ValueError("Line {} does not have enough data.".format(i+1))
            # creating Shoe object based on the object constructor
            shoe = Shoe(split[0],split[1],split[2],split[3],split[4])
            # appending Shoe object to the shoe_list
            shoe_list.append(shoe)
        #closing text file
        inventory.close()
    # handling error in case file can't be read
    except Exception as e:
        print("An error occurred while reading the data:", str(e))

# function that creates new shoe object and adds it to the text file 
def capture_shoes():
    # getting user input for each attribute of the shoe object
    country = input("Enter the country of production:\n\n")
    code = input("Enter the code for the product:\n\n")
    product = input("Enter the name of the product:\n\n")
    cost = input("Enter the cost of the product:\n\n")
    quantity = input("Enter the quantity of the product:\n\n")
    # creating new shoe object
    shoe = Shoe(country, code, product, cost, quantity)
    # appending object to the shoe_list
    shoe_list.append(shoe)
    # writing changes to inventory.txt file
    with open("inventory.txt", "w") as inventory:
        # writing first line to the file as we skipped reading this line previosly
        inventory.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inventory.write(str(shoe) + "\n")

# function that gives us overview of the stock list
def view_all():
    # using tabulate modul here in order to create table report
    shoe_l = [str(shoe).split(",") for shoe in shoe_list]
    # header of the table report
    headers = ["COUNTRY", "CODE", "PRODUCT", "COST", "QUANTITY"]
    #printing report
    print(tabulate(shoe_l, headers= headers, tablefmt="mixed_grid"))

# restocking item that is lowest on stock by adding 10 units to it 
def re_stock():
    # setting lowest item as first item in the list
    lowest_item = int(shoe_list[0].quantity)
    # iterating through shoe_list
    for item in shoe_list:
        # casting quantity for each item to Int
        q = int(item.quantity)
        #comparing each subsequent item and assigning to lowest_item
        if q < lowest_item:
            lowest_item = q
            # assigning item with lowest quantity to the new variable Lowest_item_shoe
            lowest_item_shoe = item
    print(f"The item with with lowest stock is {lowest_item_shoe}\n")
    while True:
        # asking user if the want to restock item with lowest quantity
        confirmation = input("Do you want to restock this item? YES/NO\n\n")
        if confirmation.lower() == "yes":
            # if user wants to restock then we add 10 to the quantity for the lowest item and cast it to string
            lowest_item_shoe.quantity = str(lowest_item + 10)
            # opening inventory.txt and writing whole file again to capture changes
            with open("inventory.txt", "w") as inventory:
                inventory.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    inventory.write(str(shoe) + "\n")
            break
        # if user selects no we break out
        elif confirmation.lower() == "no":
            break
        else:
            # if user doesn't enter yes or no we bring him back to the beginning of the while Loop
            print("You entered a wrong value, please proceed with YES or NO.")
            continue
# function that is searching for item based on the code
def search_shoe():
    while True:
        # asking user to enter a code for item they want to search
        code = input("Please enter the code for the item\n\n")
        # iterating through shoe_list
        for shoe in shoe_list:
            # comparing user input with database to find matching code
            if shoe.code == code:
                print("\n")
                # returning object with matching code
                return shoe
        else:
            # handling error if user enters wrong code/code that is not in the list
            print("You entered an invalid code, please try again")
            continue
# function that is calculating and displaying value for each item in the stock list
def value_per_item():
    # using string interpolation in order to transform data to the format that tabulate modul can use to display data/LIST
    value = [[str(int(shoe.cost) * int(shoe.quantity)) + "$" + " " + shoe.product] for shoe in shoe_list]
    headers = ["TOTAL VALUE PER ITEM IN $"]
    print(tabulate(value, headers= headers, tablefmt="grid"))
# function that finds item with highest quantity and displays it to the user
def highest_qty():
    # setting first item in the list as highest quantity item
    highest_item = int(shoe_list[0].quantity)
    # iterating through the list
    for item in shoe_list:
        # getting quantity for each item
        q = int(item.quantity)
        # comparing quantities and assigning the highest one
        if q > highest_item:
            highest_item = q
            # assigingin new variable highest_item_shoe to the item with highest quantity
            highest_item_shoe = item
    # letting user know that this item is on sale so we can reduce quantity
    print(f"{highest_item_shoe.product} is on sale")
#==========Main Menu=============
# menu that exicutes each function declared in the program
def main_menu():
    read_shoes_data()
    while True:
        print("""
        Main Menu:
        1. Add new item
        2. View all items
        3. Re-stock item
        4. Search for an item
        5. Calculate value per item
        6. Quit
        """)
        # asking user to choose 1 of the options:
        choice = input("Enter the number of your choice:\n\n")
        # option that is adding new item and handling possible error
        if choice == "1":
            try:
                capture_shoes()
            except Exception as e:
                print("An error occurred:", str(e))
        # option that prints stock list and handling possible error
        elif choice == "2":
            try:
                view_all()
            except Exception as e:
                print("An error occurred:", str(e))
        # option that is restocking lowest quantity item and handles possible error
        elif choice == "3":
            try:
                re_stock()
            except Exception as e:
                print("An error occurred:", str(e))
        # option that searches for item based on code and handles possible error
        elif choice == "4":
            try:
                shoe = search_shoe()
                print(shoe)
            except Exception as e:
                print("An error occurred:", str(e))
        # option that calculates value per item and handles possible error
        elif choice == "5":
            try:
                value_per_item()
            except Exception as e:
                print("An error occurred:", str(e))
        # option to exit the program
        elif choice == "6":
            break
        # else statement that is handling any other possible error and bringing back to the menu
        else:
            print("Invalid choice, please try again.")

# calling main function that runs the program
main_menu()
