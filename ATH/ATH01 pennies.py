# Name: Zhiyuan Chang
# Computing ID: vgs3qt
# This is your starter code for At-Home Coding Exercise 1
# file must be named pennies.py
# The purpose is to write a function that returns the number of pennies (cents) required for change

# Write the num_pennies function here, including docstring:

def num_pennies(itemCost, amtPaid):
    """
    This function produce the penny needed for the customer. It only calculates the penny, not other type like quarter.
    :param itemCost: The cost of the item. The second value in the calculation.
    :param amtPaid: The amount you have. The first value in the calculation.
    :return: The number of penny (pennies) needed.
    """
    x = float(itemCost)
    y = float(amtPaid)
    a = x * 100
    b = y * 100
    c = b - a
    d = c % 5
    e = int(d)
    f = str(e)
    return f


# main program
# DO NOT EDIT anything after this point
print("This program will calculate the number of pennies required for change.")
itemCost = input("Enter the cost of the item: ")
amtPaid = input("Enter the amount paid: ")
pennies = num_pennies(itemCost, amtPaid)
print("If you paid $" + amtPaid + " for something that costs $" + itemCost + " you will need " + pennies + " pennies.")
