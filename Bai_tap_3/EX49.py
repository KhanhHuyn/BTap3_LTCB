# 49. Write a Python program to count and display vowels in text.
def vowels_count(s):
    vowels = {"a":0, "e":0, "i":0, "u":0, "o":0}
    for c in s:
        if c in vowels:
            vowels[c] += 1

    for c in vowels:
        if vowels[c] > 0:
            print(f"{c} {vowels[c]}")


my_string = input("Enter your string: ")
vowels_count(my_string)