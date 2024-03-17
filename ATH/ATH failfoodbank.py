# Name: Zhiyuan Chang
# Computing ID: vgs3qt

def maxServed(fptr, year, served):
    """
    Somehow the autotester cannot read the file, I think. I runned the examples from the example and they are all good.
    :param fptr: A already opened file that can be directly used by the function.
    :param year: The year you want to compare
    :param served: 0, 1, 2; three different types of compare you want to employ.
    :return: The city. 
    """
    dict = {}
    compare = 0
    result = " "
    if served == 0:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if string[3] == "Households Served":
                    compare = 0
                elif string[3] == "":
                    compare = 0
                elif string[2] in dict:
                    dict[string[2]] = dict[string[2]] + int(string[3])
                else:
                    dict[string[2]] = int(string[3])
        for k, v in dict.items():
            if int(v) > compare:
                compare = v
                result = k
    elif served == 1:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if string[4] == "Individuals Served":
                    compare = 0
                elif string[4] == "":
                    compare = 0
                elif string[2] in dict:
                    dict[string[2]] = dict[string[2]] + int(string[4])
                else:
                    dict[string[2]] = int(string[4])
        for k, v in dict.items():
            if int(v) > compare:
                compare = v
                result = k
    elif served == 2:
        for item in fptr:
            string = item.strip().split(',')
            if string[0] == str(year):
                if string[6] == "Children Served via non-federal child nutrition programs":
                    compare = 0
                elif string[6] == "":
                    compare = 0
                elif string[2] in dict:
                    dict[string[2]] = dict[string[2]] + int(string[6])
                else:
                    dict[string[2]] = int(string[6])
        for k, v in dict.items():
            if int(v) > compare:
                compare = v
                result = k
    return result