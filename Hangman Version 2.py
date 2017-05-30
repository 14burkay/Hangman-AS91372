#Kayla Burton
#6/05/17

import random  #Used to chosen a random word from set list
#Setting up the modules for hangman     

def random_word():
    words = ["skyline", "detonator", "believable", "bridge", "apple", "playground", "daisy", "zombie", "graveyard", "binocular", "mountain", "analyse"]
    global chosen_word #So chosen_word can be acessed outside of module
    chosen_word = random.choice(words).lower() #chosen random word
    global guess_word #So guess_word can be acessed outside of module
    guess_word = []#empty list
    for letter in chosen_word:
        guess_word.append("_") # Has one _ for each letter of random word
    unjoin_word = " ".join(guess_word) #separates the _ 
    print(unjoin_word, chosen_word)#Take out chosen_word

#cheaks is uses guess has a correct input
def guess(already_guessed):
    guess = True
    while guess != False: #keeps looping until the user inputs a correct input
        global players_guess
        players_guess = input("Guess a letter ")
        if len(players_guess) > 1: # check the input is only one letter
            print("That is more than one letter. Please try again.")
                
        elif players_guess in already_guessed: # check it letter hasn't been guessed already
            print("You have already guessed that letter. Please try again.")
            
        elif players_guess not in alphaphet: #checks the input is a letter 
            print("That isn't a letter, please try again. ")
        else:
            print("You guessed the letter {}. ".format(players_guess))
            already_guessed.append(players_guess) #adds players guess to a list so it cant be guessed again
            guess = False
            return already_guessed
                        
#Alphaphet is used to make sure the user doesn't input a number            
alphaphet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
already_guessed = []
players_attempts = 10
unjoin_word = None
HANGMAN = ["00000000000000000",
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
while replay != True:
    play_again = input("Do you want to play hangman? yes/no ").lower()
    if play_again == "yes":
        print("Let's play")
        name = input("What is your name? ")
        print("""Welcome {}, to hangman.
If you don't know how to play the rules are simple,
you must try to guess a random word, letter by letter,
you have 10 wrong guesses. If you guess the word before
your attempts run out then you win.
Good luck and have fun
        """.format(name))
        
        print(HANGMAN[0])
        print("""
This is your word to guess""")
        random_word()

        if "_" in guess_word or attempts != 0:
            guess(already_guessed)
            
            for letter in range(len(chosen_word)):
                if players_guess == chosen_word[letter]:
                    guess_word[letter] = players_guess
                    joined_word = " ".join(guess_word)
                    print(joined_word)

            if players_guess not in chosen_word:
                players_attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - players_attempts])
                print("""
That letter isn't in the word, you now have {} attempts left""".format(players_attempts))
    
        else:
            print("You win")
        
    elif play_again == "no": #incorecct users input
        print("Have a nice day.")
        break
    else:
        print("That isn't a yes or a no, please try again. ")






























































































