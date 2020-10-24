import random

words = ["list", "tuple","comprenhensions"]

def random_word(word):
  #This function returns a random word from a list
  # arg:
    # list word
  # return
    # word
  random_w =random.choice(word)
  return (random_w)
  
hangman = [
  '''+---+
     |   |
     |
     |
     |
     |
     |
     |
     
     --------
     --------
  '''
]
