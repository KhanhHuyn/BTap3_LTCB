# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
my_string = input("Enter your string: ")
words = my_string.split(" ")
print(words)