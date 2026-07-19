# 2. Loan Approval Engine
# Write a program to input:
# •	monthly salary
# •	credit score
# •	existing loan amount
# •	employment type
# Rules:
# •	Approve immediately if salary > 80000, credit score > 750, and existing loan < 20000
# •	Approve with caution if salary > 50000 and credit score > 650
# •	Reject if credit score < 600
# •	Else put under manual review

salary = float(input("Enter Monthly Salary: "))
credit_score = int(input("Enter Credit Score: "))
existing_loan = float(input("Enter Existing Loan Amount: "))
employment_type = input("Enter Employment Type (Private/Government/Self-employed): ")

if salary > 80000 and credit_score > 750 and existing_loan < 20000:
    print("\nLoan Status: APPROVED IMMEDIATELY")

elif salary > 50000 and credit_score > 650:
    print("\nLoan Status: APPROVED WITH CAUTION")

elif credit_score < 600:
    print("\nLoan Status: REJECTED")

else:
    print("\nLoan Status: MANUAL REVIEW REQUIRED")