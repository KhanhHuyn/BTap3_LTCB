# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

def last_part_before(string, char):
    string_split = string.split(char)
    return string_split[0]
myString = input("Enter your string: ")


specified_char = input("Enter your specified character to split: ")
print(last_part_before(myString, specified_char))
