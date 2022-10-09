income = float(input("Enter the annual income: "))

tax = 0
tax_limit = 85528

if income < tax_limit:
    tax = (income * 0.18) - 556.2
    if tax < 0:
        tax = 0
else:
    tax = 14839.2 + (0.32 * (income-tax_limit))

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
