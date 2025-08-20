# 33. Write a Python program to print the following integers with zeros to the left of the specified
# width.

def add_zero(num_list, width):
    for num in num_list:
        print(str(num).zfill(width))


n = int(input("Enter number of integers: "))
w = int(input("Enter width: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Enter integer number {i+1}: ")))
add_zero(nums, w)
