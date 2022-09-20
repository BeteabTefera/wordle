'''
Author: Beteab D. Tefera
Discription: A Text based wordle game similar to that made by NewYork Times Magazine. The game randomly picks a five letter word called the Wordle
and the user goal is to figure it out in the specific tries they get.
However this one comes with two differences. First the player can choose difficulty levels(level 1 = 10 tries, level 2 = 5 tries, level 3 = 3 tries),
and second, the user cannot guess the same word again.

I have enjoyed coding this, and I will make it a GUI based soon using pygame modules. Look forward to that!
'''

import random

WORD_LIST = open("wordle_words.txt")
WORD_LIST = WORD_LIST.read()
WORD_LIST = WORD_LIST.split()

#MYSTERY_WORD = random.choice(WORD_LIST)
MYSTERY_WORD = 'shook'

def main():
    num_tries = 0
    printline()
    print("WELCOME TO WORDLE!!")
    print("Guess the mystery five-letter word, known as the “wordle”!!\n")
    print("Choose your level: Level 1 (Easy) | Level 2 (Medium) | Level 3 (Hard)")
    printline()
    print("Press 1, 2, 3 for each respective level.")
    printline()
    start = True

    while start:
        found_letters= ['_','_','_','_','_']
        not_in_word = set()
        user_input = input("Select Level: ")
        wordSep = list(MYSTERY_WORD)
        prev_word = set()
        num_tries = 0
        temp_word =''
        try:
            int(user_input)
        except ValueError:
            print("Can only press 1, 2, 3 for each respective level.")
            printline()
        else:
            user_input = int(user_input)
            if user_input in [1,2,3]:
                if user_input == 1:
                    print("level 1(EASY) has been selected,\nyou will have 10 turns to guess the right word.")
                    num_tries = 10
                    printline()
                    while  num_tries != 0:
                        if num_tries == 3:
                            print(f"WARNING: You Only Have {num_tries} turns Left!")
                        
                        
                        
                        user_input = input("Guess Word: ")
                        user_input = user_input.lower()
                        
                        #while loop for already said words
                        while True:
                            if user_input in prev_word:
                                print("you have already guessed this word!")
                                printline()
                                user_input = input("Guess Word: ")
                            else:
                                break

                        try:
                            int(user_input)
                            print("Can only use letters")
                            printline()
                        except ValueError:              
                            if len(user_input) == 5:
                                if user_input in WORD_LIST and user_input == MYSTERY_WORD:
                                    print("\nCONGRATULATIONS!!! YOU HAVE FOUND THE WORD")
                                    printline()
                                    break

                                elif user_input in WORD_LIST and user_input != MYSTERY_WORD:
                                    user_input = list(user_input)
                                    for i in user_input:
                                        if i in wordSep:
                                            temp_word = ''.join(wordSep)
                                            temp_index = temp_word.find(i)
                                            wordSep.remove(i)
                                            wordSep.insert(temp_index,"_")
                                            found_letters[temp_index] = i
                                            temp_word = ''.join(wordSep)
                                            wordSep = list(temp_word)
                                            
                                        else:
                                            not_in_word.add(i)
                                    print(f"Found letters: {found_letters}")
                                    print(f"Letters not in word: {sorted(not_in_word)}")
                                    printline()
                                    found_letters= ['_','_','_','_','_']
                                    prev_word.add("".join(user_input))
                                    wordSep = list(MYSTERY_WORD)
                                else:
                                    print("\nWord not in wordlist")
                                    printline()
                                    num_tries +=1
                            else:
                                print("This game only allows five letter words")
                                num_tries +=1
                            num_tries -= 1

                    if num_tries == 0:
                        print("GAMEOVER!!!! You Are Out Of Turns!!")
                    while True:
                        user_input = input("Would You Like To Play Again? (y/n): ")
                        user_input.lower()
                        if user_input == "y":
                            start = True
                            prev_word.clear()
                            break
                        elif user_input == "n":
                            start = False
                            break
                        else:
                            print("Please chooses Y/N")
                    continue


                elif user_input == 2:
                    print("level 2(MIDEUM) has been selected,\nyou will only have 5 turns to guess the right word.")
                    num_tries = 5
                    printline()
                    while  num_tries != 0:
                        if num_tries == 3:
                            print(f"WARNING: You Only Have {num_tries} turns Left!")
                        
                        
                        
                        user_input = input("Guess Word: ")
                        user_input = user_input.lower()
                        
                        #while loop for already said words
                        while True:
                            if user_input in prev_word:
                                print("you have already guessed this word!")
                                printline()
                                user_input = input("Guess Word: ")
                            else:
                                break

                        try:
                            int(user_input)
                            print("Can only use letters")
                            printline()
                        except ValueError:              
                            if len(user_input) == 5:
                                if user_input in WORD_LIST and user_input == MYSTERY_WORD:
                                    print("\nCONGRATULATIONS!!! YOU HAVE FOUND THE WORD")
                                    printline()
                                    break

                                elif user_input in WORD_LIST and user_input != MYSTERY_WORD:
                                    user_input = list(user_input)
                                    for i in user_input:
                                        if i in wordSep:
                                            temp_word = ''.join(wordSep)
                                            temp_index = temp_word.find(i)
                                            wordSep.remove(i)
                                            wordSep.insert(temp_index,"_")
                                            found_letters[temp_index] = i
                                            temp_word = ''.join(wordSep)
                                            wordSep = list(temp_word)
                                            
                                        else:
                                            not_in_word.add(i)
                                    print(f"Found letters: {found_letters}")
                                    print(f"Letters not in word: {sorted(not_in_word)}")
                                    printline()
                                    found_letters= ['_','_','_','_','_']
                                    prev_word.add("".join(user_input))
                                    wordSep = list(MYSTERY_WORD)
                                else:
                                    print("\nWord not in wordlist")
                                    printline()
                                    num_tries +=1
                            else:
                                print("This game only allows five letter words")
                                num_tries +=1
                            num_tries -= 1

                    if num_tries == 0:
                        print("GAMEOVER!!!! You Are Out Of Turns!!")
                    while True:
                        user_input = input("Would You Like To Play Again? (y/n): ")
                        user_input.lower()
                        if user_input == "y":
                            start = True
                            prev_word.clear()
                            break
                        elif user_input == "n":
                            start = False
                            break
                        else:
                            print("Please chooses Y/N")
                    continue    


                elif user_input == 3:
                    print("level 3(HARD) Difficulty has been selected,\nyou will only have 3 turns to guess the right word.")
                    num_tries = 3
                    printline()
                    while  num_tries != 0:
                        if num_tries == 1:
                            print(f"WARNING: You Only Have {num_tries} turn Left!")
                         
                        user_input = input("Guess Word: ")
                        user_input = user_input.lower()
                        
                        #while loop for already said words
                        while True:
                            if user_input in prev_word:
                                print("you have already guessed this word!")
                                printline()
                                user_input = input("Guess Word: ")
                            else:
                                break

                        try:
                            int(user_input)
                            print("Can only use letters")
                            printline()
                        except ValueError:              
                            if len(user_input) == 5:
                                if user_input in WORD_LIST and user_input == MYSTERY_WORD:
                                    print("\nCONGRATULATIONS!!! YOU HAVE FOUND THE WORD")
                                    print("OUTSTANDING!! You Have Managed To Guess The Word In Difficulty MODE!!")
                                    print("You are a CHAMPION!!!")
                                    printline()
                                    break

                                elif user_input in WORD_LIST and user_input != MYSTERY_WORD:
                                    user_input = list(user_input)
                                    for i in user_input:
                                        if i in wordSep:
                                            temp_word = ''.join(wordSep)
                                            temp_index = temp_word.find(i)
                                            wordSep.remove(i)
                                            wordSep.insert(temp_index,"_")
                                            found_letters[temp_index] = i
                                            temp_word = ''.join(wordSep)
                                            wordSep = list(temp_word)
                                            
                                        else:
                                            not_in_word.add(i)
                                    print(f"Found letters: {found_letters}")
                                    print(f"Letters not in word: {sorted(not_in_word)}")
                                    printline()
                                    found_letters= ['_','_','_','_','_']
                                    prev_word.add("".join(user_input))
                                    wordSep = list(MYSTERY_WORD)
                                else:
                                    print("\nWord not in wordlist")
                                    printline()
                                    num_tries +=1
                            else:
                                print("This game only allows five letter words")
                                num_tries +=1
                            num_tries -= 1

                    if num_tries == 0:
                        print("GAMEOVER!!!! You Are Out Of Turns!!")
                    while True:
                        user_input = input("Would You Like To Play Again? (y/n): ")
                        user_input.lower()
                        if user_input == "y":
                            start = True
                            prev_word.clear()
                            break
                        elif user_input == "n":
                            start = False
                            break
                        else:
                            print("Please chooses Y/N")
                    continue    
            else:
                print("Can only choose one of the following: 1 | 2 | 3")
                printline()               


        
def printline():
    print("_"*75)
    print(" ")

             
if __name__ == "__main__":
    main()
