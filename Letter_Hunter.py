'''Coded by Vishwa R Panchal'''
import random
from random_word import RandomWords
import string
from colorama import init ,Style ,Fore


init()
rw = RandomWords()
word = rw.get_random_word()
wordSize = len(word)
hidden = ['-']*wordSize

def guessBegin(word):
    attempts = 0
    while "-" in hidden:
        print(Fore.WHITE+"\nGuess the word: "+" ".join(hidden))
        guessletter = (input("Enter the letter: "))
        if not guessletter:
            print(Fore.RED + "No input provided. Please enter a letter.")
            continue
        if guessletter in word:
            for i in range(wordSize):
                if word[i] == guessletter:
                    hidden[i] = guessletter
            print(Fore.GREEN+"Correct!!")
        else:
            print(Fore.RED+"Incorect")
        attempts += 1
        if attempts%10==0:
            choice = input(Fore.CYAN+"\nWould you like to see the solution? (Y/N): ")
            if choice.lower() == 'y':
                solutionBegin(word)
            else:
                continue

    solution_key = "".join(hidden)
    print("The word is: "+Fore.YELLOW+solution_key)

def playAgain():
    while True:
        choice = input(Fore.YELLOW+"\nPlay again? (Y/N): ")
        if choice.lower() == 'y':
            global word, wordSize, hidden
            word = rw.get_random_word()
            wordSize = len(word)
            hidden = ['-'] * wordSize
            guessBegin(word)
        elif choice.lower() == 'n':
            print(Fore.CYAN+"Thank you for playing!")
            break
        else:
            print(Fore.RED+"Invalid choice. Please enter 'Y' or 'N'.")



def solutionBegin(word):
    tries = string.ascii_lowercase
    while "-" in hidden:

        for alphabet in tries:
            if alphabet in word:
                for i in range(wordSize):
                    if word[i] == alphabet:
                        hidden[i] = alphabet


print(Fore.YELLOW+"***** WORD HUNTER GAME*****\n")
print(Fore.MAGENTA+"Each Dash stands for each letter.\n")

while True:
    guessBegin(word)
    playAgain()
    break

init(autoreset=True)
