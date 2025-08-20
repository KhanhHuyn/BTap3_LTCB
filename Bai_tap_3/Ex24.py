# 24. Write a Python program to check whether a string starts with specified characters.
def starting_chars_check(string, chars):
    if chars == string[:len(chars)]:
        return True
    return False


my_string = input("Enter your string: ")
starting_chars = input("Enter the starting characters: ")
if not starting_chars_check(my_string, starting_chars):
    print("No, your string does not start with", starting_chars)
else:
    print("Yes, your string starts with", starting_chars)
