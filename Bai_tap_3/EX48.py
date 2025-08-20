# 48. Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
def swap_commas_dots(s):
    s = s.replace(",", "#")
    s = s.replace(".", ",")
    s = s.replace("#", ".")
    return s;

my_string = input("Enter your string: ")
print(swap_commas_dots(my_string))