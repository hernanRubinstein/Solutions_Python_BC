import random

num_ran = random.randrange(1,21)
count_i = 0
while True:
    guess_curr = int(input("please write your guess"))
    count_i += 1
    if guess_curr == count_i:
        print("GREATTT!")
        print(f"Guesses #: {count_i} ")
        break
    if guess_curr > count_i:
        print("Too bad! \n your guess was too big - PLEASE RETRY")
    if guess_curr < count_i:
        print("Too bad! \n your guess was too small - PLEASE RETRY")