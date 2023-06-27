print("Pythagoras' Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = input("Enter your choice (1-3): ")

if choice == '1':
    side_b = float(input("Enter the length of side B: "))
    side_c = float(input("Enter the length of side C: "))
    side_a = (side_c ** 2 - side_b ** 2) ** 0.5
    print(f"The length of side A is: {side_a}")
elif choice == '2':
    side_a = float(input("Enter the length of side A: "))
    side_c = float(input("Enter the length of side C: "))
    side_b = (side_c ** 2 - side_a ** 2) ** 0.5
    print(f"The length of side B is: {side_b}")
elif choice == '3':
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    side_c = (side_a ** 2 + side_b ** 2) ** 0.5
    print(f"The length of side C is: {side_c}")
else:
    print("Invalid choice. Please select a valid option (1-3).")

print("** End **")