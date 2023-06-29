#Part 1 - Using while loops:

#Task 1 - Squares:

number = 1

while number <= 100:
    square = number ** 2
    print(number, ":", square)
    if square > 2000:
        break
    number += 1
#Task 2 - Factorial:
number = int(input("Enter an number: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial:", factorial)

#Task 3 - Investment:
investment = 100
target_value = 1000
interest_rate = 0.10
years = 0

while investment < target_value:
    investment += investment * interest_rate
    years += 1

print("Years to reach target value:", years)

#Task 4 - Input an Integer Between Two Limits:
min_value = 1
max_value = 100
attempts = 0

while attempts < 3:
    number = int(input("Enter an number between 1 and 100: "))
    if min_value <= number <= max_value:
        print("Valid number:", number)
        break
    attempts += 1

if attempts == 3:
    print("None")

# Task 5 - Count Vowels:
word = input("Enter a word: ")
vowel_count = 0

for char in word:
    if char.lower() in "aeiouAEIOU":
        vowel_count += 1

print("Number of vowels:", vowel_count)

#Task 6 - Exam Average:
math_mark = int(input("Enter the math mark (0-100): "))
english_mark = int(input("Enter the English mark (0-100): "))
ict_mark = int(input("Enter the ICT mark (0-100): "))

marks = [math_mark, english_mark, ict_mark]
average = sum(marks) / len(marks)

print("Average mark:", average)

if average >= 65:
    print("Pass")
else:
    print("Fail")

#part 2

# Task 1 - Squares
for number in range(1, 101):
    square = number ** 2
    print(number, ":", square)
    if square > 2000:
        break


# Task 2 - Factorial
num = int(input("Enter an integer: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial)
