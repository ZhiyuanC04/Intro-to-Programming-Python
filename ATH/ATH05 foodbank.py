# Name: Zhiyuan Chang
# Computing ID: vgs3qt

def maxServed(fptr, year, served):
    """
    Read the file and then return the city that served the most people based on the year.
    :param fptr: A already opened file that can be directly used by the function.
    :param year: The year you want to compare
    :param served: 0, 1, 2; three different types of compare you want to employ.
    :return: The city. 
    """
    compare = 0
    result = ""
    count = 0
    if served == 0:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if string[3] == "Households Served":
                    count += 1
                elif string[3] == "":
                    count += 1
                elif int(string[3]) > compare:
                    compare = int(string[3])
                    result = string[2]
    elif served == 1:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if string[4] == "Individuals Served":
                    count += 1
                elif string[4] == "":
                    count += 1
                elif int(string[4]) > compare:
                    compare = int(string[4])
                    result = string[2]
    elif served == 2:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if "Children" in string[4]:
                    count += 1
                elif string[6] == "":
                    count += 1
                elif int(string[6]) > compare:
                    compare = int(string[6])
                    result = string[2]
    return result