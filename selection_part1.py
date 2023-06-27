#age = int(input("please enter your age"))
#if age >= 18:
#    print("you are in category A")
#if age >= 16:
#    print("you are in category B")
#if age <= 16:
#    print("you are in category C")


#age = int(input("please enter your age:"))
#if age >= 18:
#    print("you are in category A")
#elif age >= 16:
#    print("you are in category B")
#else:
#    print("you are in category C")

# Calculator task

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Calculator Menu:")
print("1. Add +")
print("2. Subtract -")
print("3. Multiply *")
print("4. Divide /")
print("5. Square s")

choice = input("Enter your choice (1-5): ")

if choice == '1':
    result = num1 + num2
    print("The sum is:", result)
elif choice == '2':
    result = num1 - num2
    print("The difference is:", result)
elif choice == '3':
    result = num1 * num2
    print("The product is:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == '5':
    result1 = num1 ** 2
    result2 = num2 ** 2
    print("Square of", num1, "is:", result1)
    print("Square of", num2, "is:", result2)
else:
    print("Invalid choice. Please select a valid option (1-5).")

print("** End **")
