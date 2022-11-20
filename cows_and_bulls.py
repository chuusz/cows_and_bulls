import random

"""
Create a program that will play the 'cows and bulls' game with the user. The game works like this:
Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a 'cow'.
For every digit the user guessed correctly in the wrong place is a 'bull.'
Every time the user makes a guess, tell them how many 'cows' and 'bulls' they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""

def compare(guess, number):
    guess = [int(i) for i in str(guess)]
    number = [int(i) for i in str(number)]
    cows, bulls = 0, 0

    for i in range(4):
        if guess[i] == number[i]:
            cows += 1
            guess[i], number[i] = None, None
    for i in range(4):
        if guess[i] == None:
            continue
        elif guess[i] in number:
            number[number.index(guess[i])] = None
            bulls += 1
    return f"\n{cows} {'cow' if cows == 1 else 'cows'} & {bulls} {'bull' if bulls == 1 else 'bulls'}\n"


def cows_and_bulls():
    number = random.randint(1000, 9999)
    guesses = 1
    while True:
        try:
            guess = int(input("Gues number between 1000 to 9999:\n"))
            if 999 < guess < 10000:
                if guess == number:
                    print(f"You guessed it after {guesses} {'guess' if guesses == 1 else 'guesses'}!")
                    break
                else:
                    print(compare(guess, number))
                    guesses += 1
                    continue
            else:
                print('Wrong number, try again!\n')
                continue
        except:
            print('It is not a number, please try again!')
            continue


if __name__ == "__main__":
    cows_and_bulls()
