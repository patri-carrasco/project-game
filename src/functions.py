import random




def is_letter(char):
  '''
  This function chekc the char is in alphabet
      arg:
          char
      return 
          letter : True or False
  '''
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letter = False
  if char in alphabet:
      letter = True

  return (letter)

def random_word(word):
  '''
      This function returns a random word from a list
        arg:
            word
        return
              random word 
  '''
  random_w =random.choice(word)
  return (random_w)

def pos_char(char,word):
    '''
        This function looks for the character in the word and returns the positions where they appear 
            args :
                char
                word
            return
                positions
    '''
    pos = []
    for i in enumerate(word):
        if i[1] == char:
            pos.append(i[0])

    return (pos)


def get_empty_word(size):
  arr = []
  for i in range(size):
    arr += '-'
  return arr

def print_game_status(wrong, right,board):
  print(hangman[len(wrong)-1])
  print(board)
  print(f'Mistake char {wrong}')
  print(f'Right {right}')

hangman = [
'''
+---+
|   |
|
|
|
|
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|   
| 
|
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|   |
|   |
|   |
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|  /|
|   |   
|   
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|  /|\
|   |
|   
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|  /|\
|   |
|  /
|
|
--------
--------
''',
'''
+---+
|   |
|   O
|  /|\
|   |
|  / \
|
|
--------
--------
'''
]
