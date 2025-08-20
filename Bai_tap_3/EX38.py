# 38. Write a Python program to count occurrences of a substring in a string
my_string = input("Enter your string: ")
substr = input("Enter your substring: ")
occurrence = my_string.count(substr)
print(f"Your substring occurrences: {occurrence}")