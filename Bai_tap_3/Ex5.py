# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string

myString1 = input("Enter your first string: ")
myString2 = input("Enter your second string: ")

print(myString2[0:2] + myString1[2] + " " + myString1[0:2] + myString2[2])
