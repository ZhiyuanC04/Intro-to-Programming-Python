# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def mean_all(table):
    """
    The mean_all function should take in a “table”, which will be in the form of a list of lists of numbers
    (float or int types). The function should return the arithmetic mean1 of all of the numbers in the list
    of lists. The value returned should be a float type.
    :param table: a list of lists of numbers (float or int types).
    :return: the arithmetic mean1 of all of the numbers in the list of lists.
    """
    sum = 0
    count = 0
    for item in table:
        for each in range(len(item)):
            a = item[each]
            sum += a
            count += 1
    mean = sum / count
    return mean

def mean_by_row(table):
    """
    The mean_by_row function should take in a “table”, which will be in the form of a list of lists of numbers
    (float or int types). The function should return a list containing the arithmetic means of each row’s values.
    A “row” is a sublist in the list of lists. For the specific example above, the function would return a list
    of the average enrollment in each semester across the different CS111X variations.
    :param table: a list of lists of numbers (float or int types).
    :return: a list of the average enrollment in each semester across the different CS111X variations.
    """
    result = []
    for item in table:
        sum = 0
        count = 0
        for each in range(len(item)):
            a = item[each]
            sum += a
            count += 1
        mean = sum / count
        result.append(sum / count)
    return result

def mean_by_col(table):
    """
    The mean_by_col function should take in a “table”, which will be in the form of a list of lists of numbers
    (float or int types). The function should return a list containing the arithmetic means of each column’s
    values. A “column” is all of the values at a particular index in each of the sublists. For the specific
    example above, the function would return a list of the average enrollment in each CS111X variation across
    the different semesters.
    :param table: a list of lists of numbers (float or int types).
    :return: a list of the average enrollment in each CS111X variation across the different semesters.
    """
    result = []
    x = 0
    for num in range(len(table[x])):
        sum = 0
        count = 0
        for item in table:
            a = item[num]
            sum += a
            count += 1
        mean = sum / count
        result.append(mean)
    return result