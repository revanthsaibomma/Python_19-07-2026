# 15. Subscription Renewal Prediction
# Input:
# •	monthly usage
# •	missed payments
# •	support tickets count
# •	satisfaction score
# Rules:
# •	High usage + high satisfaction → Likely renew
# •	Low usage + many complaints → High churn risk
# •	Missed payments > threshold → Payment risk
# •	Else moderate renewal probability

monthly_usage = float(input("Enter Monthly Usage (hours): "))
missed_payments = int(input("Enter Number of Missed Payments: "))
support_tickets = int(input("Enter Support Tickets Count: "))
satisfaction = float(input("Enter Satisfaction Score (1-10): "))

if monthly_usage > 50 and satisfaction >= 8:
    print("Prediction : Likely to Renew")
    print("Reason : High usage and high satisfaction.")

elif monthly_usage < 20 and support_tickets > 5:
    print("Prediction : High Churn Risk")
    print("Reason : Low usage with many complaints.")

elif missed_payments > 3:
    print("Prediction : Payment Risk")
    print("Reason : Too many missed payments.")

else:
    print("Prediction : Moderate Renewal Probability")
    print("Reason : Customer has average usage and payment history.")