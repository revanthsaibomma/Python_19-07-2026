# Problem Statement: Employee Loan Eligibility System Using if-elif-else
# A bank wants to create a Python application to check whether a working professional is eligible for a personal loan.
# The loan decision will be based on:
# •	Applicant’s age 
# •	Monthly salary 
# •	Total work experience 
# •	Credit score 
# •	Existing monthly EMI 
# Eligibility Rules
# 1.	The applicant’s age must be between 21 and 58 years. 
# 2.	The applicant must have at least 2 years of work experience. 
# 3.	The applicant’s credit score must be at least 650. 
# 4.	Loan eligibility will be decided using the following salary rules: 
# Monthly Salary	Maximum Loan Eligibility
# ₹25,000–₹39,999	₹2,00,000
# ₹40,000–₹59,999	₹5,00,000
# ₹60,000–₹99,999	₹10,00,000
# ₹1,00,000 or above	₹15,00,000
# 5.	The existing EMI should not be more than 40% of the monthly salary. 
# 6.	When any mandatory condition is not satisfied, the application should be rejected with an appropriate reason. 
# Expected Input
# Enter applicant name:
# Enter age:
# Enter monthly salary:
# Enter work experience in years:
# Enter credit score:
# Enter existing monthly EMI:
# Expected Output Example
# Applicant Name: Rahul Sharma
# Loan Application Status: Eligible
# Maximum Loan Amount: ₹5,00,000
# Or:
# Applicant Name: Rahul Sharma
# Loan Application Status: Rejected
# Reason: Credit score is below 650.


name = str(input("Enter applicant name: "))
age = int(input("Enter age: "))
monthly_salary = float(input("Enter monthly salary: "))
work_experience = float(input("Enter work experience in years: "))
credit_score = int(input("Enter credit score: "))
existing_emi = float(input("Enter existing monthly EMI: "))
if age < 21 or age > 58:
    print("The application is rejected.")
    print("Reason: Age criteria not met.")
elif work_experience < 2:
    print("The application is rejected.")
    print("Reason: Work experience is below 2 years.")
elif credit_score < 650:
    print("The application is rejected.")
    print("Reason: Credit score is below 650.")
else:
    if 25000 <= monthly_salary <= 39999:
        max_loan = 200000
    elif 40000 <= monthly_salary <= 59999:
        max_loan = 500000
    elif 60000 <= monthly_salary <= 99999:
        max_loan = 1000000
    elif monthly_salary >= 100000:
        max_loan = 1500000
    else:
        max_loan = 0
    
    if existing_emi > 0.4 * monthly_salary:
        print("The application is rejected.")
        print("Reason: Existing EMI is more than 40% of monthly salary.")
    else:
        print(f"Applicant Name: {name}")
        print(f"Loan Application Status: Eligible")
        print(f"Maximum Loan Amount: ₹{max_loan:,}")
