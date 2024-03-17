# This is Zhiyuan Chang's work. My computing ID is vgs3qt. Thankyou.

def the_random_num1(x):
    a = x * 2
    b = a + 5
    c = b * 50
    return c
def the_random_num2(y):
    a = y + Birthday
    b = a - Born_year
    return b
random_num = int(input("Pick a number between 1 and 10: "))
Cal1 = the_random_num1(random_num)
# Cal = Calculation.
Birthday = int(input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: "))
Born_year = int(input("Enter the year that you were born: "))
Cal2 = the_random_num2(Cal1)
Cal3 = Cal2 % 100
Cal2 = str(Cal2)
Cal3 = str(Cal3)
print("The magic number is " + '"' + Cal2 + '"' + "." + " That means you are " + Cal3 + "!")
