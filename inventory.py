"""
    This task uses object-oriented programming and functions to read an external text file, inventory.txt,
    to create shoe objects which can be viewed and updated. Additional shoe objects can also be created
    by the user and all changes are then rewritten back to the inventory.txt file.
    The menu format allows for an interactive and well-formatted experience and structured, readable code that is
    sectioned in 3 parts: the class & methods, functions and the menu.
"""

# ======== The beginning of the class ==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass


    def get_cost(self):
        print(f'Code:\t\t{self.code}\n\n- Cost:\t\t\tR {self.cost}.00')
        pass


    def get_quantity(self):
        print(f'- Quantity:\t\t{self.quantity}')
        pass

    def update_quantity(self, new):
        self.quantity = new


    def __str__(self):
        # requirement: staff searches products by code therefore prioritise product code
        shoe_output = f'''
CODE: {self.code}
-   Product:\t{self.product}
-   Country:\t{self.country}
-   Cost:\t\tR {self.cost}.00
-   Quantity:\t{self.quantity}
'''
        return shoe_output


# ============= Shoe list ===========

# store a list of objects of shoes - most functions will use this list

shoe_list = []


# ========== Functions Outside the Class ==============

# reads 'inventory.txt', makes Shoe objects and adds them to 'shoe_list'
def read_shoes_data(a):     # 'a' will be the list of shoe objects

    # read task file
    with open("inventory.txt", "r") as file:

        # create empty item list
        i_list = []

        # format file data to add to item list
        for lines in file:
            # strip lines into a list of entries
            temp = lines.strip("\n")

            # split each entry into a sublist of data that can be indexed (2-D)
            temp = temp.split(",")

            # append entries to item list
            i_list.append(temp)



    try:
        # loop through item list and assign a variable to each index
        for count, data in enumerate(i_list, 1):
            country = i_list[count][0]
            code = i_list[count][1]
            product = i_list[count][2]
            cost = int(i_list[count][3])            # enter cost as an integer value
            quantity = int(i_list[count][4])        # enter quantity as an integer value

            # create an object with the Shoe class with data from the item list (i_list)
            shoe_object = Shoe(country, code, product, cost, quantity)

            # append each shoe object to the list 'a' which is the shoe list
            a.append(shoe_object)

    except IndexError:  # avoid index error
        print(f'==== Read Shoe Data: Complete. ====\n')  # return confirmation message

    # return updated list of shoe objects.
    return a

    pass


# loops through most updated shoe_list and formats entries for 'inventory.txt'
def update_file():

    # begin with writing heading to file (will then append updated data afterward)
    # NB must be outside the For loop!
    with open("inventory.txt", "w") as file:
        heading = 'Country,Code,Product,Cost,Quantity'
        file.write(heading)

    # now format data for file with loop through shoe_list:
    for obj in shoe_list:
        # assign variables to format data in txt file.
        country = obj.country
        code = obj.code
        product = obj.product
        cost = obj.cost
        quantity = obj.quantity

        # format data for txt file
        entry = f'\n{country},{code},{product},{cost},{quantity}'

        # write entries to file
        with open('inventory.txt', 'a') as file:
            file.write(entry)


# creates new shoe entry from user inputs, adds them to shoe_list and updates 'inventory.txt'
def capture_shoes():
    try:
        # request user input for new shoe entry
        print("Please enter the following information:")
        country = input('Country:\t').title()
        code = input('Code:\t').upper()
        product = input('Product:\t').title()
        print('Please enter the Rand Value of the shoes without cents or currency. Eg: 1500')
        cost = int(input('Cost:\tR '))
        print('Please enter the quantity of the shoes as a numerical value. Eg: 23')
        quantity = int(input('Quantity:\t'))

        # create new Shoe object
        new_shoe = Shoe(country, code, product, cost, quantity)

        # append new shoe object to shoe list
        shoe_list.append(new_shoe)

        # update inventory.txt file with added shoe
        update_file()

    except ValueError:
        print('Please enter the values correctly.')

    # confirmation text
    print('Your shoe has been added successfully.')
    pass


# views all shoe objects in shoe_list and outputs them in a formatted list
def view_all():
    underline = '==================================='  # for formatting
    for count, shoe in enumerate(shoe_list, 1):
        print(f'''{underline}\n\n# {count}\n{shoe}''')
    print(underline)

    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


# displays shoes in need of restock with option to update shoe quantity. Also updates 'inventory.txt'
def re_stock():
    # create a list of quantities (to compare shoe quantities)
    quantity = []
    for obj in shoe_list:
        quantity.append(obj.quantity)  # append object quantities to this list

    # sort shoes in ascending order
    quantity.sort()

    # match quantity number to the shoe object
    for obj in shoe_list:

        if obj.quantity == quantity[0]:
            # this outputs the shoe\s with the lowest quantity
            underline = '==================================='  # for formatting
            print(f'\nRESTOCK PRODUCT:\n{underline}\n {obj}\n{underline}\n')


            # request quantity update
            submenu = input('Would you like to update the quantity of this shoe?\n[y/n]:\t').lower()

            # if yes, update object quantity
            if submenu == 'y':
                while True:
                    try:
                        # request new quantity value
                        new_quantity = int(input("\nNew Quantity (as a numerical value):\t"))

                        # update object quantity with class method - also auto-updates in shoe list
                        obj.update_quantity(new_quantity)

                        # output to user
                        print(f'\nUPDATED PRODUCT:\n{underline}\n {obj}\n{underline}\n')
                        break

                    except ValueError:
                        print('Oops! Please enter a number value only.')

                # run update file function to update inventory.txt
                update_file()

            # if no, return to main menu
            elif submenu == 'n':
                break

            else:
                print('Oops! Please enter "y" to edit or "n" to return to the main menu.\n')

    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

# restocks items by code and updates 'inventory.txt'
def code_re_stock():

    # create a list of codes (to determine if searched code is in database)
    codes = []
    for obj in shoe_list:
        codes.append(obj.code)      # append object codes to this list

    while True:
        # request code from user
        search_code = input("Search Product Code:\t").upper()

        # check validity of search code in shoe list
        if search_code in codes:

            # match search code
            for obj in shoe_list:
                # if valid, update the quantity value
                if obj.code == search_code:

                    # this outputs the shoe data in a readable format
                    underline = '==================================='
                    print(f'\nRESTOCK PRODUCT:\n{underline}\n {obj}\n{underline}\n')

                    while True:
                        try:
                            # request new quantity value
                            new_quantity = int(input("\nNew Quantity (as a numerical value):\t"))

                            # update object quantity with class method - also auto-updates in shoe list
                            obj.update_quantity(new_quantity)

                            # output to user
                            print(f'\nUPDATED PRODUCT:\n{underline}\n{obj}\n{underline}\n')
                            break

                        except ValueError:
                            print('Oops! Please enter a number value only.')

                    # run update file function to update inventory.txt
                    update_file()

            break

        # if not valid, display error and re-request code
        elif search_code not in codes:
            print(f'- Product "{search_code}" is not found. Please enter a different code.\n')

    pass


# searches for shoe code in database(shoe_list) by requesting a search code and outputting shoe data
def search_shoe():

    # create a list of codes (to determine if searched code is in database)
    codes = []
    for obj in shoe_list:
        codes.append(obj.code)      # append object codes to this list

    while True:
        # request code from user
        search_code = input("Search Product Code:\t").upper()

        # check validity of search code in shoe list
        if search_code in codes:
            # if valid, output the shoe data with the corresponding Product Code
            for obj in shoe_list:
                if search_code == obj.code:
                    print(obj)
            underline = '==================================='  # for formatting
            print(underline)
            break

        # if not valid, display error message and re-request code
        elif search_code not in codes:
            print(f'- Product "{search_code}" is not found. Please enter a different code.\n')

    pass



    """
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    """


# calculates and displays the total value (cost x price) of each item in database.
def value_per_item():

    # format heading for data
    underline = '==================================='  # for formatting
    print(f'VALUE PER ITEM')

    # calculate value for each item
    for count, obj in enumerate(shoe_list):
        print(f'{underline}\n\n{count+1}.', end=" ")

        # call methods from class to get output of cost and quantity
        # this outputs a condensed version of out 'view all' data
        obj.get_cost()
        obj.get_quantity()

        # assign variables to integer values of cost and quantity (to calculate)
        cost = int(obj.cost)
        quantity = int(obj.quantity)

        # calculate and display value to user
        print(f'- Value:\t\tR {cost * quantity}.00\n')

    # format end of outputted value list
    print(underline)

    pass


# sorts objects in ascending order by quantity and displays the item with the highest quantity (for sale).
def highest_qty():

    # create a list of quantities (to compare shoe quantities)
    quantity = []
    for obj in shoe_list:
        quantity.append(obj.quantity)  # append object quantities to this list

    # sort shoes in descending order
    quantity.sort(reverse=True)

    # match quantity number to the shoe object
    for obj in shoe_list:

        # this outputs the shoe\s with the highest quantity
        if obj.quantity == quantity[0]:
            underline = '==================================='  # for formatting
            print(f'\nDUE FOR SALE:\n{underline}\n{obj}\n{underline}')

    pass


# run read shoes
read_shoes_data(shoe_list)

# ========== Main Menu =============

# greeting
greeting = "\nT H E   S N E A K E R   R O O M .\nFor Sneakerheads. By Sneakerheads.\n"
print(greeting)


# main menu
while True:

    menu_options = f'''\n===== MAIN MENU =====\n
Please select one of the following options: [1-6 or e]\n
\t1 - View All Items
\t2 - Search Item by Code
\t3 - Restock Item by Code
\t4 - Item Due for Restock
\t5 - Item Due for Sale
\t6 - Capture New Item
\t7 - Show item Values
\te - Exit

\t:\t'''

    menu = input(menu_options).lower()

    # view all shoes
    if menu == '1':
        view_all()

    # search item by code
    elif menu == '2':
        search_shoe()

    # restock item by code
    elif menu == '3':
        code_re_stock()

    # item due for restock - ie item with the lowest quantity
    elif menu == '4':
        re_stock()

    # show item due for sale  - ie item with the highest quantity
    elif menu == '5':
        highest_qty()

    # capture a new item
    elif menu == '6':
        capture_shoes()

    # show value per item
    elif menu == '7':
        value_per_item()

    # exit
    elif menu == 'e':
        print('\nGoodbye! :D')
        break

    # error message
    else:
        print("Oops! Only enter a numerical value from 1-6 or 'e' to Exit.\n")

# end
