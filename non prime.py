A = int(input("Enter the starting number A: "))
B = int(input("Enter the ending number B: "))

for num in range(A, B + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(num, end=" ")
                break
