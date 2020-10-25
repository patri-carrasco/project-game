import src.functions as fn

#words = ["list", "tuple","comprenhensions"]
words = ["list", "moco"]

#get random word from a list
word = fn.random_word(words)
print(word)

print("Hi, wellcome  to hagnman game's")


#game(word)


right = []
wrong = []


board = fn.get_empty_word(len(word))
#game



while len(wrong)<len(fn.hangman) and '-' in board:
  #check if char is alphabet
  char_n = input("Enter a char ")

  # get the char in lowercase
  char = char_n.lower()
  fn.print_game_status(wrong,right,board)

  if  not fn.is_letter(char_n):
    char_n = input("Enter a correct char ")
  
  

  pos_char_word = []

  if fn.pos_char(char,word)!= []:
    pos_char_word = fn.pos_char(char,word)
    
    right.append(char)
    print(right)
    
    for i in pos_char_word:
      board[i] = char
    
   
  else:
    wrong.append(char)
  

  
  
  












