# 41. Write a Python program to strip a set of characters from a string
def strip_chars(string, chars):
    return "".join(c for c in string if c not in chars)

my_string = input("Enter your string: ")
stripped_chars = input("Enter your set of characters to be strip: ")

print(strip_chars(my_string, stripped_chars))