prime_count = sum(1 for num in [int(input()) for _ in range(int(input()))] if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1)
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", int(input()) - prime_count)
