the_word = input("a word: ")
the_word = the_word.lower()
blank = "_".join(the_word) + "_"
print(blank[1::2])
z = 1

def function():
    global blank
    global z
    # print(blank[1::2])
    guess_1 = input("Guess a letter: ")
    guess_1 = guess_1.lower()
    if guess_1 in blank:
        print("There is " + str(guess_1) + "!")
        if guess_1 in blank:
            blank = blank.replace(guess_1 + "_", guess_1 * 2)
    else:
        if z < 5:
            print("Nope; that's a mistake number", z)
            z += 1
        else:
            print("Nope; that's a mistake number", z)
            print("no more chance.")
            z += 1
    print(blank[1::2])

while "_" in blank and z <= 5:
    function()
