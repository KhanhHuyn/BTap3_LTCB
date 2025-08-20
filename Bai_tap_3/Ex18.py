# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt

def first_three(string):
    if (len(string) < 3):
        return string
    return string[:3]


myString = input("Enter your string: ")
print(first_three(myString))
