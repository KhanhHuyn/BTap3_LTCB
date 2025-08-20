 # 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
# string. If the string length is less than 2, return the empty string instead.
myString = input("Enter your string: ")
if len(myString >= 2):
    print(myString[:2] + myString[-2:])
else:
    print("Empty String")