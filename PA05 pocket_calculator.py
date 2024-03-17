# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def get_value():
    """
    Simply returns the int representing the current value stored in the calculator.
    :return: the current value stored in the global scope.
    """
    global current_stored
    return current_stored

def clear(optional = 0):
    """
    Reset the second and third globals mentioned above to their initial values, set the first and fourth globals mentioned above to the argument’s int value and its str representation.
    :param optional: An random int value.
    :return: either clear the values in global value (and change to the input int if needed)
    """
    global current_stored
    global recent_operation
    global recent_argument
    global series_calculation
    current_stored = int(optional)
    recent_operation = ""
    recent_argument = 0
    series_calculation = ""
    y = str(optional)
    series_calculation = y
    return int(optional)

def step(string, argument):
    """
    calculation function.
    :param string: the + - * //, one of the four
    :param argument: An int.
    :return: the calculator’s current int value.
    """
    global current_stored
    global recent_operation
    global recent_argument
    global series_calculation
    if string == "+":
        current_stored = int(current_stored) + int(argument)
    elif string == "-":
        current_stored = int(current_stored) - int(argument)
    elif string == "*":
        current_stored = int(current_stored) * int(argument)
    elif string == "//":
        current_stored = int(current_stored) // int(argument)
    recent_operation = string
    recent_argument = int(argument)
    series_calculation = "(" + str(series_calculation) + ")" + str(string) + str(argument)
    return int(current_stored)

def repeat():
    """
    Repeat its last calculation step.
    :return: The calculator’s current int value.
    """
    global current_stored
    global recent_operation
    global recent_argument
    global series_calculation
    if recent_operation != "":
        x = step(recent_operation, recent_argument)
    else:
        x = current_stored
    return x

def get_expr():
    """
    :return: A str representing the current expression.
    """
    global series_calculation
    return series_calculation

current_stored = 0  # int
recent_operation = ""  # str
recent_argument = 0  # int
series_calculation = "0"  # str