# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
def count_repeated_chars(s):
    mp = {}
    for c in s:
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1;
    for c in mp:
        print(f"{c} {mp[c]}")


my_string = input("Enter your string: ")
count_repeated_chars(my_string)