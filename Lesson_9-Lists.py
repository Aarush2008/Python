# First describe whats inside the list
# Write values inside square brackets
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
# Lists can have strings(Karen likes Jim), numbers(1), or booleans(false or true)
print(friends)
# Friends will be pasted in the terminal
# Index(first, second, thrid ect) start with 0
# Kevin is 0 while Karen is 1 and Jim is 2
print(friends[0])
# Just going to print out Kevin because he is 0
# Negitives is used to access items from the back of the list.
print(friends[-1])
# -1 is Jim because he is the last in the list.
# To index one thing and everything after add a number :
print(friends[1:])
# A number colon another number will index the things from the first number to the thing before the second number
# Karen and Jim will show in the terminal as Karen is 1 and everything after that is Jim
print(friends[1:3])
# Karen and Jim will be in the terminal as Karen is 1 and Jim is 2 and 3 does not show
print(friends[1])
# This will show Mike becuse we replaced Karen which is one with the name Mike
