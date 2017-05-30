#Kayla Burton
#20/05/17

import random  #Used to chosen a random word from set list
#Setting up the modules for hangman     

def random_word(unjoins_word):
    list_of_words = ["skyline", "detonator", "believable", "bridge", "apple", "playground", "daisy", "zombie",
                     "graveyard", "binocular", "mountain", "analyse", "jazz", "abomination", "paralysed", "hallucination",
                     "arrogant", "horizon", "vinyl", "hibernation", "collorbone", "diamond", "bamboo", "echo", "charismatic",
                     "oxygen","pixel", "wave", "wizard", "kayak", "banjo", "kiwifruit", "pneumonia", "puppy", "walkway",
                     "fox"]
    global chosen_word #So chosen_word can be acessed outside of module
    chosen_word = random.choice(list_of_words) #choses random word
    global guess_word #So guess_word can be acessed outside of module
    guess_word = []#empty list
    for letter in chosen_word:
        guess_word.append("_") # Has one _ for each letter of random word
    unjoins_word = " ".join(guess_word) #separates the _ 
    return unjoins_word

#cheaks is uses guess has a correct input
def users_guess(already_guessed):
    guess = True
    while guess != False: #keeps looping until the user inputs a correct input
        global players_guess
        players_guess = input("""
Please guess a letter """)
        if len(players_guess) > 1: # check the input is only one letter
            print("Please try again, your input was more than one letter. ")
                
        elif players_guess in already_guessed: # check it letter hasn't been guessed already
            print("Please try again, you have already guessed that letter.")
            
        elif players_guess not in alphabet: #checks the input is a letter 
            print("Please try again, that input isn't a letter,  ")
        else:
            print("""
You guessed the letter {}. """.format(players_guess))
            already_guessed.append(players_guess) #adds players guess to a list so it cant be guessed again
            guess = False
            return already_guessed

def display(players_attempts):
    repeat = True
    while repeat != False:
        if "_" in guess_word: #repeats until word has been guessed 
            if players_attempts != 1: #or until attempts have run out
                users_guess(already_guessed) 
            
                for letter in range(len(chosen_word)): #loops through chosen word
                    if players_guess == chosen_word[letter]: 
                        guess_word[letter] = players_guess
                unjoins_word = " ".join(guess_word)
                print(unjoins_word) #prints the _ version of the random_word but unjoins the _ _
                        

                if players_guess not in chosen_word: #players choice isn't in the word
                    players_attempts -= 1
                    print(HANGMAN_SYMBOLS[(len(HANGMAN_SYMBOLS) - 1) - players_attempts]) #Shows picture of hangman when players choice is wrong
                    print("""
The letter {} isn't in the word, you now have {} attempts left""".format(players_guess, players_attempts))
                    print(unjoins_word)#prints the word again
            else:
                print(HANGMAN_SYMBOLS[10])
                print("Sorry you have zero attempts left, your word was {} ".format(chosen_word))
                repeat = False#when attempts run out, the game ends 
    
        else:
            print("Congratulations you guessed the word, {} ".format(chosen_word))
            repeat = False#if the users guesses the word 
                        
#Alphaphet is used to make sure the user doesn't input a number            
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
already_guessed = []
unjoins_word = None
HANGMAN_SYMBOLS = ["00000000000000000", #shows the ten attempts in picture form
"""
    1           
    1           
    1          
    1           
    1           
    1            
    1             
    1           
    1            
    1                    
    1
 00000000000000000
""",
"""
222222222222222222
    1           2
    1           
    1           
    1           
    1           
    1            
    1             
    1           
    1            
    1                    
    1
 00000000000000000
 """,
 
"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1           
    1            
    1             
    1           
    1            
    1                    
    1
 00000000000000000
""",
 
"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1           4
    1           4 
    1           4  
    1           
    1            
    1                    
    1
 00000000000000000
""",
"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          54
    1         5 4 
    1        5  4  
    1           
    1            
    1                    
    1
 00000000000000000
""",
 
"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          546
    1         5 4 6
    1        5  4  6
    1           
    1            
    1                    
    1
 00000000000000000
""",

"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          546
    1         5 4 6
    1        5  4  6
    1          7 
    1         7   
    1        7            
    1
 00000000000000000
""",

"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          546
    1         5 4 6
    1        5  4  6
    1          7 8
    1         7   8
    1       7       8
    1
 00000000000000000
""",
"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          546
    1         5 4 6
    1        5  4  6
    1          7 8
    1         7   8
    1        7     899
    1
 00000000000000000
""",

"""
222222222222222222
    1           2
    1           3
    1          3 3
    1           3
    1          546
    1         5 4 6
    1        5  4  6
    1          7 8
    1         7   8
    1      107     899
    1
 00000000000000000
"""]

replay = False
while replay != True: #will repeat the game if the user wants to play again
    play_again = input("Do you want to play hangman? yes/no ").lower()
    if play_again == "yes":
        print("Let's play")
        players_attempts = 10
        already_guessed = []#resets the list when replayed 
        user_name = input("What is your name? ") #Introduction and rules
        print("""Welcome {}, to hangman.
If you don't know how to play the rules are simple,
you must guess a random word, letter by letter,
you have 10 wrong guesses. If you guess the word before
your attempts run out then you win.
Good luck and have fun
        """.format(user_name))
        
        print(HANGMAN_SYMBOLS[0]) 
        print("""
This is your word to guess""")
        print(random_word(unjoins_word))
        display(players_attempts)

    elif play_again == "no": #if the user doesn't want to play again
        print("Have a nice day.")
        replay = True#used instead of break 
    
    else:
        print("That isn't a yes or a no, please try again. ")
        
        






























































































