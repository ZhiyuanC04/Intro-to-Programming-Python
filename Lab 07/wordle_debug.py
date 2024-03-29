import random
import wordle_helper

#Create dictionary and screen elements [DON'T CHANGE THIS SECTION]
common_words_list, five_letter_dictionary = wordle_helper.create_dictionary()
keyboard = wordle_helper.make_keyboard() # A string formatted into a keyboard
empty_guess = wordle_helper.make_empty_guess() # A string formatted to represent an empty guess
guesses = [empty_guess, empty_guess, empty_guess, empty_guess, empty_guess, empty_guess]

def enter_guess(guess, guess_num):
    '''
    Updates the screen colors (guesses and keyboard) to reflect the user's guess
    '''
    global secret_word, keyboard, guesses

    guess = guess.upper()
    color_guess = " "
    #Update keyboard and build color_guess
    for i in range(0, 5):
        letter = guess[i]

        # The buttons are just colored strings. They make up the keyboard and the color_guess
        light_button = wordle_helper.make_button(letter, "light_gray")
        dark_button = wordle_helper.make_button(letter, "dark_gray")
        yellow_button = wordle_helper.make_button(letter, "yellow")
        green_button = wordle_helper.make_button(letter, "green")

        if letter.lower() not in secret_word:
            # Wrong letter
            color_guess += dark_button + " "
            keyboard = keyboard.replace(light_button, dark_button)
        elif letter.lower() != secret_word[i]:
            #Correct letter wrong spot
            color_guess += yellow_button + " "
            keyboard = keyboard.replace(light_button, yellow_button)
        else:
            #Correct letter correct spot
            color_guess += green_button + " "
            keyboard = keyboard.replace(light_button, green_button)
            keyboard = keyboard.replace(yellow_button, green_button)

    # Update guess list by replacing blank guess with the color_guess
    guesses[guess_num] = color_guess


#Initialize game
randomize = input("Would you like to randomize your secret word (y/n)? ")
if randomize == "y" or randomize == "Y" or randomize == "yes" or randomize == "Yes":
    choice = random.randint(1, len(common_words_list)-1)
    secret_word = common_words_list[choice]
else:
    possible = False
    while not possible:
        secret_word = input("Please enter the secret word: ").lower().strip()
        possible = secret_word in five_letter_dictionary
        if not possible:
            print("Please enter a valid 5-letter word.")

#Begin gameplay
guess_num = 1
guessed_correctly = False
while guess_num < 6 and guessed_correctly is False:
    wordle_helper.print_screen(guesses, keyboard)
    # Ask for a guess until a valid guess is given
    possible = False
    while not possible:
        guess = input("Please guess a word: ").lower().strip()
        possible = guess in five_letter_dictionary
        if not possible:
            print("Please enter a valid 5-letter word.")

    enter_guess(guess, guess_num)

    if guess == secret_word:
        guessed_correctly = True
    guess_num += 1

#Game over
wordle_helper.print_screen(guesses, keyboard)
if guessed_correctly == True:
    print("\nYou won! You correctly guessed the word in " + str(guess_num) + "/6 tries!")
else:
    print("\nYou ran out of tries. The secret word was \"" + secret_word + ".\"")