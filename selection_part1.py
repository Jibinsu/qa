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

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Calculator App!")

while True:
    print("\nSelect an operation:")
    print("1. Add +")
    print("2. Subtract -")
    print("3. Multiply * ")
    print("4. Divide / ")

    choice = input("Enter your choice (1-4):")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")
