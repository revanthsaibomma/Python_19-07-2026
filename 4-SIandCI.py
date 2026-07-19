principle = int(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principle * rate * time) / 100
print(simple_interest)
print("The simple interest is:", simple_interest)
print(f"The simple interest is: {simple_interest}")
compound_interest = principle * (1 + rate / 100) ** time - principle
print(compound_interest)
print("The compound interest is:", compound_interest)
print(f"The compound interest is: {compound_interest}")