# 47. Write a Python program to lowercase the first n characters in a string
def to_lower_first_n_chars(s, n):
    return s[:n].lower() + s[n:]


my_string = input("Enter your string: ")
n = int(input("Enter the number of first characters you want to convert to lowercase: "))

print(to_lower_first_n_chars(my_string, n))