# String are plain text that stores data
# Backslash "n" is used to sperate the words
print("Aarush\nPatel")
print("Aarush\"Patel")
print("Aarush\nPatel")
phrase = "Aarush Patel"
# Phrase is  variable
# Below is something called concatentation, which is when you add on another string
print(phrase + "is cool")
# Functions are blocks of code used to performe specific operations
phrase = "Aarush Patel"
print(phrase.lower())
# "Phrase.lower makes all words into lower case"
# "Phrase.upper makes all words into upper case"
print(phrase.upper())
# Below is a true of false statment
# The answer will be false as Aarush Patel is not upper case
print(phrase.isupper())
print(phrase.islower())
# Below the phrase will first be converted to upper case
# Then the phrase will agree that the words are in upper case
print(phrase.upper().isupper())
# Below, len stands for length
# It will tell you how many character are inside of the string
print(len(phrase))
# Python always starts with 0
# In Aarush Patel, A will be 0, a will be 1, r will be 2, ect.
print(phrase[0])
print(phrase.index("Pate"))
# Below will replace the first name, Aarush, with the second name, Bhagya
print(phrase.replace("Aarush", "Bhagya"))
