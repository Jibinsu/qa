def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif 1150 <= salary <= 34500:
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000:
        return 4350 + ((salary - 34500) * 0.4)
    else:
        return 50730 + ((salary - 150000)) * 0.45

# Prompt the user for salary input
salary = float(input("Enter your salary: £"))

# Calculate the tax for the inputted salary
tax_amount = getIncomeTax(salary)

# Display the tax amount
print("Tax amount for £{} salary: £{}".format(salary, tax_amount))
