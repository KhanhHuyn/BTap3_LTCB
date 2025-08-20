# 37. Write a Python program to display a number in left, right, and center aligned with a width of
# 10.
def aligned(num):
    s = str(num)
    print("Left aligned:", s.ljust(10))
    print("Right aligned:", s.rjust(10))
    print("Center aligned:", s.center(10))


n = float(input("Enter a number: "))
aligned(n)