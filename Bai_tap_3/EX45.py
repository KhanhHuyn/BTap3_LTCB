# 45. Write a Python program to check whether a string contains all letters of the alphabet.
def contains_all_alphabet(s):
    letters = set(ch.lower() for ch in s if ch.isalpha())
    return len(letters) == 26

my_string = input("Enter your string: ")
if (contains_all_alphabet(my_string)):
    print("YES")
else:
    print("NO")