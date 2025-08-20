# 11. Write a Python program to remove characters that have odd index values in a given string.

myString = input("Enter your string")
newString = ""
for i in range(len(myString)):
    if (i % 2 == 0):
        newString += myString[i]
print(newString)
