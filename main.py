import src.functions as fn

words = ["list", "tuple","comprenhensions","lambda","loop","for","while","functionw"]
word = fn.random_word(words)
print("Hi, wellcome  to hagnman game's")
right = []
wrong = []
board = fn.get_empty_word(len(word))

while True:
  fn.clear()
  pos_char_word = []
  fn.print_game_status(wrong,right,board)
  char = fn.get_char()
  if fn.pos_char(char,word)!= []:
    pos_char_word = fn.pos_char(char,word)

    if char in right:
      print("Char inserted before")
      continue
    right.append(char)
    print(right)
    for i in pos_char_word:
      board[i] = char
  else:
    if char in wrong:
      print("Char inserted before")
      continue
    wrong.append(char)
  if len(wrong)>=len(fn.hangman):
    print('You loose, LOOSER')
    break
  if not '-' in board:
    print("You won, BEGINER'S LUCK")
    break
  
  
  
  












