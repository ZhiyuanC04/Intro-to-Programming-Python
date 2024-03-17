# Computing ID: vgs3qt
# Name: Zhiyuan Chang

dic = {} # key = each state, value = the winner of that state

def add_state(name, votes):
    """
    The expected behavior of this function is to store the election results for the given state within
    the global dict.
    :param name:  A string to distinguish this state from others
    :param votes: A dictionary whose keys are the names of each candidate (string) and whose vallues
    are the number of votes (int) each candidate received in this state
    :return: Nothing
    """
    global dic
    compare = ["null", "zero"]
    for k,v in votes.items():
        if compare[0] == "null":
            compare.remove("null")
            compare.remove("zero")
            compare.append(k)
            compare.append(v)
        elif compare[1] < v:
            compare.remove(compare[0])
            compare.remove(compare[0])
            compare.append(k)
            compare.append(v)
    winner = compare[0]
    dic[name] = winner
    return

def winner(college):
    """
    The expected behavior of this function is to read the election results from the global dictand
    determine the nationwide winner from the information in parameter college.
    :param college: A dictionary whose keys are the names of each state (string) and whose values
    are the amount of electoral votes (int) the state has
    :return: The name of that candidate or no winner
    """
    global dic
    memory = {}
    compare = ["null", "zero"]
    count = 0
    for all in dic.values():
        memory[all] = 0
    for k,v in college.items():
        if k in dic:
            memory[dic[k]] += v #+ memory[dic[k]]
    for x,y in memory.items():
        if compare[0] == "null":
            compare.remove("null")
            compare.remove("zero")
            compare.append(x)
            compare.append(y)
        elif compare[1] < y:
            compare.remove(compare[0])
            compare.remove(compare[0])
            compare.append(x)
            compare.append(y)
    for m,n in college.items():
        if m in dic:
            count += n
    if compare[1] != "zero":
        if compare[1] > count/2:
            return compare[0]
        else:
            return "No Winner"
    else:
        return "No Winner"

def clear():
    """
    The clear function should simply reset any global variable(s) to their initial value(s).
    :return: Nothing
    """
    global dic
    mem = []
    for keys in dic.keys():
        mem.append(keys)
    for i in mem:
        del dic[i]
    return