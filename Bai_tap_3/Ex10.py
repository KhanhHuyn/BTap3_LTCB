# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged.

myString = input("Enter your string:")
myString = myString[-1] + myString[1:-1] + myString[0]
print(myString)
