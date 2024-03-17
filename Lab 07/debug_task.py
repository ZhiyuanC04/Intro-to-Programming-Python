# Higher/Lower Game

print("Think of a number between 1 and 100 and I'll guess it.")
num_guesses = int(input("How many guesses do I get? "))
upper_bound = 100
lower_bound = 1
cheating = False
guess_count = 0

guess = 50
answer = input("Is the number higher, lower, or the same as 50? ")
while answer != "same" and guess_count < num_guesses:
    guess_count += 1
    if answer == "higher":
        lower_bound = guess + 1
    elif answer == "lower":
        upper_bound = guess - 1
    if upper_bound <= lower_bound:
        print("Wait; how can it be both higher than " + str(lower_bound) + " and lower than " + str(upper_bound) + "?")
        cheating = True
    elif guess_count < num_guesses:
        guess = (lower_bound + upper_bound) // 2
        answer = input("Is the number higher, lower, or the same as " + str(guess) + "? ")

if guess_count >= num_guesses and not cheating:
    answer = int(input("I lost; what was the answer? "))
    if answer < lower_bound:
        print("That can't be; you said it was higher than " + str(lower_bound) + "!")
    if answer > upper_bound:
        print("That can't be; you said it was lower than " + str(upper_bound) + "!")
    else:
        print("Well played!")
elif not cheating:
    print("I won!")