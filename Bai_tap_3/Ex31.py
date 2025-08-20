# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.

def formatted_num(num_list):
    for i in num_list:
        print(f"{i:+.2f}")


n = int(input("Enter the number of numbers: "))
my_num_list = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    my_num_list.append(num)

formatted_num(my_num_list)
