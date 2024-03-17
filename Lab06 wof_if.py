the_word = input("a word: ")
the_word = the_word.lower()
blank = "_".join(the_word) + "_"
print(blank[1::2])


def function():
    global blank
    global z
    # print(blank[1::2])
    guess_1 = input("Guess a letter: ")
    guess_1 = guess_1.lower()
    if guess_1 in blank:
        print("There is " + str(guess_1) + "!")
        if guess_1 == "a":
            blank = blank.replace("a_", "aa")
        elif guess_1 == "b":
            blank = blank.replace("b_", "bb")
        elif guess_1 == "c":
            blank = blank.replace("c_", "cc")
        elif guess_1 == "d":
            blank = blank.replace("d_", "dd")
        elif guess_1 == "e":
            blank = blank.replace("e_", "ee")
        elif guess_1 == "f":
            blank = blank.replace("f_", "ff")
        elif guess_1 == "g":
            blank = blank.replace("g_", "gg")
        elif guess_1 == "h":
            blank = blank.replace("h_", "hh")
        elif guess_1 == "i":
            blank = blank.replace("i_", "ii")
        elif guess_1 == "j":
            blank = blank.replace("j_", "jj")
        elif guess_1 == "k":
            blank = blank.replace("k_", "kk")
        elif guess_1 == "l":
            blank = blank.replace("l_", "ll")
        elif guess_1 == "m":
            blank = blank.replace("m_", "mm")
        elif guess_1 == "n":
            blank = blank.replace("n_", "nn")
        elif guess_1 == "o":
            blank = blank.replace("o_", "oo")
        elif guess_1 == "p":
            blank = blank.replace("p_", "pp")
        elif guess_1 == "q":
            blank = blank.replace("q_", "qq")
        elif guess_1 == "r":
            blank = blank.replace("r_", "rr")
        elif guess_1 == "s":
            blank = blank.replace("s_", "ss")
        elif guess_1 == "t":
            blank = blank.replace("t_", "tt")
        elif guess_1 == "u":
            blank = blank.replace("u_", "uu")
        elif guess_1 == "v":
            blank = blank.replace("v_", "vv")
        elif guess_1 == "w":
            blank = blank.replace("w_", "ww")
        elif guess_1 == "x":
            blank = blank.replace("x_", "xx")
        elif guess_1 == "y":
            blank = blank.replace("y_", "yy")
        elif guess_1 == "z":
            blank = blank.replace("z_", "zz")
    else:
        print()
    print(blank[1::2])


z =

while "_" in blank:
    function()
    # z += 1

if guess_1 in blank:


# if "_" in blank:
    # function()
# else:
    # print("you r done")