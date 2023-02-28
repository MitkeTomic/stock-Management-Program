# stock-Management-Program
This program is a simple inventory management system that uses OOP as the main concept.

This program is a simple inventory management system for shoes. It allows the user to view all the items in the inventory, capture new items to the inventory, search for a particular item based on the product code, restock the item with the lowest quantity in the inventory, and exit the program.

The program uses a Shoe class to create objects with attributes such as the country of production, product code, product name, cost, and quantity. It stores these objects in a shoe_list, which serves as the inventory database.

The program reads and writes data to a text file called "inventory.txt". The file contains the first line as headers of the inventory database and each subsequent line is a record of the Shoe object attributes separated by commas.

The program uses the tabulate module to display the inventory data in a table format. It also handles errors that may occur when reading the data from the text file.

The capture_shoes() function allows the user to add new Shoe objects to the inventory. The re_stock() function restocks the item with the lowest quantity in the inventory by adding 10 units to it. The search_shoe() function searches for a particular item based on the product code entered by the user.

Overall, this program demonstrates basic file input/output operations, error handling, class and object creation, and tabulation.
