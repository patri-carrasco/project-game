import src.functions as fn

words = ["list", "tuple","comprenhensions"]

print("Hi, wellcome  to hagnman game's")
char_n = input("Enter a char ")

# get the char in lowercase
char = char_n.lower()

#get random word from a list
word = fn.random_word(words)
print(word)



