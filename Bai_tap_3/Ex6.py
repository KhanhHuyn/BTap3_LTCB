# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.

myString = input("Enter your string: ")
if (len(myString) < 3):
    print(myString)
else:
    if (myString[-3:] == "ing"):
        print(myString + "ly")
    else:
        print(myString + "ing")
