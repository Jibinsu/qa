weight = float(input("Enter weight: "))
unit = input("Enter unit (kgs/lbs): ").lower()

if unit == "kgs":
    converted_weight = weight * 2.20462
    print(f"{weight} kgs is equivalent to {converted_weight} lbs.")
elif unit == "lbs":
    converted_weight = weight / 2.20462
    print(f"{weight} lbs is equivalent to {converted_weight} kgs.")
else:
    print("Invalid unit entered. Please enter either 'kgs' or 'lbs'.")