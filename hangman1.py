import string
from words import choose_wod
from images import IMAGES
def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):

    all_letters= string.ascii_lowercase
    letters_left=""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left+=letter
    return letters_left
def ifValid(user_input):
    if len(user_input)== 1:
        return True
    if user_input.isalpha():
        return True
    else:
        return "invalid"    
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)        
def hangman(secret_word):
    name=input("enter your name->")
    print (name,"Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    j=0
    while j<1:
        user_difficulty_choice = input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
        if user_difficulty_choice=="a" or user_difficulty_choice not in ["a","b","c"]:
            print("game strat in eassy mode")
            remaining_lives = 8
            images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
            j+=1
        elif user_difficulty_choice == "b":
            remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]
            j+=1
        elif user_difficulty_choice == "c":
            remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]
            j+=1
        else:                                                                                                                                                                              
            continue
    letters_guessed = []
    count=0
    c=0
    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        print("******")
        guess =input("Please guess a letter/hint: ")
        letter = guess.lower()
        if letter=="hint":
            if count==0:
                print("your hint for this secret word is this--"+get_hint(secret_word,letters_guessed))
                count+=1
            else:
                print("hint already used")
        if letter not in get_available_letters(letters_guessed):
            continue
        if not ifValid(letter):
            continue            
        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print(IMAGES[images_selection_list_indices[c]])
            c+=1
            remaining_lives -= 1
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            # if c==len(images_selection_list_indices):
            #     print("out of move plz try again")
            #     break
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
secret_word=choose_wod()
# print(secret_word)
hangman(secret_word)