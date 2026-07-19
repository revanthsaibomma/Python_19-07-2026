# 5. Insurance Premium Decision
# Take:
# •	customer age
# •	smoking habit
# •	BMI
# •	pre-existing disease status
# Rules:
# •	High premium for smokers with age > 50
# •	Medium premium for overweight users
# •	Reject if severe pre-existing disease and age > 60
# •	Low premium for healthy young users

age = int(input("Enter Customer Age: "))
smoking = input("Is the customer a smoker? (yes/no): ").lower()
bmi = float(input("Enter BMI: "))
disease = input("Does the customer have a severe pre-existing disease? (yes/no): ").lower()

if disease == "yes" and age > 60:
    print("\nInsurance Status : Rejected")

elif smoking == "yes" and age > 50:
    print("\nPremium Category : High Premium")

elif bmi >= 25:
    print("\nPremium Category : Medium Premium")

elif age < 35 and smoking == "no" and bmi < 25 and disease == "no":
    print("\nPremium Category : Low Premium")

else:
    print("\nPremium Category : Standard Premium")