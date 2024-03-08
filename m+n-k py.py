m = int(input("enter a number"))
n = int(input("enter a number"))
k = int(input("enter a number"))
current_number = m
while current_number <= n:
    print(current_number, end=" ")
    current_number += k + 1
