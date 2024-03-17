# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def compare(list):
    """
    The function  takes as input a list of strings.
    The function should return the number of strings where
    the first and last character are the same, regardless of case.
    :param list: List of strings
    :return: number of strings where the first and last character are the same, regardless of case.
    """
    count = 0
    for i in range(len(list)):
        word = list[i]
        word = word.lower()
        if word[0] == word[-1]:
            count += 1
    return count