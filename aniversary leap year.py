year = int(input("Enter the anniversary year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The given anniversary year is a leap year.")
    print("Next anniversary:", year + 4)
else:
    print("The given anniversary year is not a leap year.")
    print("Previous anniversary:", year - 1)
