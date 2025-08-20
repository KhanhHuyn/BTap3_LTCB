# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters

def convert(string):
    cnt = 0
    for char in string[:4]:
        if char.isupper():
            cnt += 1
    if cnt >= 2:
        return string.upper()
    return string

my_string = input("Enter your string: ")
print(convert(my_string))
