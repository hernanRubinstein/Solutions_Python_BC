import random

############################################################################################################

def special_key(user_input, number):
    if user_input.lower() == 'x':
        return "Exiting Game"
    elif user_input.lower() == 'n':
        answer = input("New game? [yes/no]")
        if answer.lower() == 'yes':
            return "Restarting"
        else :
            return "Exiting Game"
    elif user_input.lower() == 's':
        print("The answer is: ", number, "You cheater")
        return "Guess again"
    else:
        return "Continue"

############################################################################################################

def evaluate_input(user_input, number, counter):
    if int(user_input) == number:
        print("GREATTT!")
        print(f"Guesses #: {counter} ")

        answer = input("New game? [yes/no]")
        if answer.lower() == 'yes':
            return "Restarting"
        else :
            return "Exiting Game"
        
    elif int(user_input) > number:
        print("Too bad! \n your guess was too big - PLEASE RETRY")
        return "Guess again"

    elif int(user_input) < number:
        print("Too bad! \n your guess was too small - PLEASE RETRY")
        return "Guess again"

############################################################################################################

def main():
    while True: # new game
        num_ran = random.randrange(1,21)
        counter = 1
        print("Rules of game: \n In each moment you can exit the game press: 'x' \n To restart press: 'n' \n To get the currect answer (Cheating :) press: 's'")
    
        while True: # internal round
            guess_curr = input("please write your guess:")
            input1 = special_key(guess_curr, num_ran)

            if input1 == "Restarting" or input1 == "Exiting Game":
                break
            
            elif input1 == "Guess again":
                continue
            
            try:
               input2 = evaluate_input(guess_curr, num_ran, counter)
               if input2 == "Restarting" or input2 == "Exiting Game":
                   break   
            except ValueError:
                print("Please enter a valid input")
                continue
            
            counter += 1
        
        if input1 == "Exiting Game" or input2 == "Exiting Game":
            break

############################################################################################################

main()