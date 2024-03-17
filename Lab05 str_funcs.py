def ellipsis(function_one):
    return print(function_one[0:2] + ".." + function_one[-2:])

def eighteen(function_two):
    return print(function_two[0:1] + str(len(function_two)-2) + function_two[-1:])

def allit(word_one, word_two):
    word_one = word_one.lower()
    word_two = word_two.lower()
    if word_one[0:1] == word_two[0:1]:
        return print("True")
    else:
        return print("False")

def between(para_one, para_two):
    length = int(len(para_two))
    a = para_one.find(para_two)
    b = para_one[(a+length):]
    c = b.find(para_two)
    if a != "None" and c != "None":
        return print(para_one[(a+length):(c+1)])
    else:
        return print('""')

def rbetween(para_one, para_two):
    x = para_one[::-1]
    y = para_two[::-1]
    length = int(len(y))
    a = x.find(y)
    b = x[(a+length):]
    c = b.find(y)
    inverse_correct = (x[(a+length):(c+a+length)])
    correct = inverse_correct[::-1]
    print(correct)

rbetween("loan me a lovely loon to look at", "lo")

