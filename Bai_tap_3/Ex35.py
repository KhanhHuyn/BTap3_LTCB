# 35. Write a Python program to display a number with a comma separator.

def display_with_comma(num):
    print(f"{num:,}")


n = int(input("Enter an integer: "))
display_with_comma(n)
