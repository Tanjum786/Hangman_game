import random
def load_words():
    f=open("words.txt","r")
    f1=f.read()
    f2=f1.split()
    # [print(f2)
    return f2
def choose_wod():
    word_list=load_words()
    secret_word=random.choice(word_list)
    secret_word=secret_word.lower()
    return secret_word
(choose_wod())