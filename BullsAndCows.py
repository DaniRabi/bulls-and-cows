import random

# set difficulty
dif = raw_input("Enter Difficulty (easy or hard): ")
while (dif != "easy") and (dif != "hard"):
        dif = raw_input("Enter Difficulty (easy or hard): ")

# 'easy' settings
lst_length = 4     # default length of number
tries = 10         # default numer of tries

# 'hard' settings
if diff == "hard":
    tries /= 2        # 5 tries
    lst_length *= 2   # 8 digits

# set hidden number
lst = []
while len(lst) < lst_length:
    x = random.randrange(1, 10)
    if x not in lst:
        lst.append(x)

# player starts guessing
while tries > 0:
    guess = []
    while len(guess) < lst_length:
        y = int(raw_input("Choose a number between 1 and 9 (Don't repeat or it won't be included)"))
        if y not in guess and ((y > 0) and (y < 10)):
            guess.append(y)
    
    # check bulls and cows
    bulls = 0
    cows = 0
    for index, item in enumerate(lst):
        if item == guess[index]:
            bulls += 1
        elif item in guess:
            cows += 1

    # print results
    print "Your guess: " + str(guess)
    print "Bulls: " + str(bulls)
    print "Cows: " + str(cows)
    
    # check winning condition
    if bulls == lst_length:
        print "You win!"
        break

    tries--

if tries = 0:
    print "You Lose"
    print "The correct answer: " + str(lst)

raw_input()