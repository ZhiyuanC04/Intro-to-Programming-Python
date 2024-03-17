# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def update(contactDict, list_of_values):
    """
    The function should attempt to process all of the values in the parameter list_of_values
    to the contactDict dictionary using the following rules and should return an error count.
    :param contactDict: A dictionary mapping names to email addresses
    :param list_of_values: A list of tuples consisting of three strings, the first representing
    the action, the second is a name and the third is an email address.
    :return: An error count.
    """
    error = 0
    for i in list_of_values:
        if i[0] == "+":
            if i[1] not in contactDict:
                contactDict[i[1]] = i[2]
            elif i[1] in contactDict:
                error += 1
        elif i[0] == "/":
            if i[1] not in contactDict:
                error += 1
            elif i[1] in contactDict:
                contactDict[i[1]] = i[2]
        elif i[0] == "-":
            if i[1] not in contactDict:
                error += 1
            elif i[1] in contactDict:
                del contactDict[i[1]]
        else:
            error += 1
            return error
    return error