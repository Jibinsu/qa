a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Finding the largest number
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

# Checking the conditions for the largest number
if largest // 2 == largest / 2:
    print("Even Number")
elif largest // 3 == largest / 3:
    print("Odd Number and a Multiple of 3")
else:
    print("Odd Number")
