import random



def random_word(word):
  #This function returns a random word from a list
  # arg:
    # list word
  # return
    # word
  random_w =random.choice(word)
  return (random_w)
  
  def is_letter(char):
    '''
    This function chekc the char is in alphabet
        arg:
            char
        return 
            letter : True or False
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = False
    if char in alphabet:
        letter = True
 
    return (letter)
    
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
