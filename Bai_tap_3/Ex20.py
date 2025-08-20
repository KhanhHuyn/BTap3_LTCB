# 20. Write a Python function to reverse a string if its length is a multiple of 4.

def my_reverse(string):
    if (len(string) % 4 == 0):
        return string[::-1]
    return "Your string's length is not a multiple of 4"


myString = input("Enter your string: ")
print(my_reverse(myString))
