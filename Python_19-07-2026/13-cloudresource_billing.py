# 4. Cloud Resource Billing System
# Input:
# •	number of compute hours
# •	storage used
# •	support plan type
# Rules:
# •	Basic plan: fixed support fee
# •	Premium plan: higher support fee but discounted compute
# •	Enterprise plan: custom rate with storage discount
# •	Final bill depends on multiple slabs

compute_hours = int(input("Enter Compute Hours: "))
storage = float(input("Enter Storage Used (GB): "))
plan = input("Enter Support Plan (Basic/Premium/Enterprise): ").lower()

if compute_hours <= 100:
    compute_charge = compute_hours * 5
elif compute_hours <= 300:
    compute_charge = compute_hours * 4
else:
    compute_charge = compute_hours * 3

storage_charge = storage * 2

if plan == "basic":
    support_fee = 500

elif plan == "premium":
    support_fee = 1000
    compute_charge = compute_charge * 0.90

elif plan == "enterprise":
    support_fee = 2000
    storage_charge = storage_charge * 0.80

else:
    support_fee = 0
    print("Invalid Plan")

total_bill = compute_charge + storage_charge + support_fee

print("Compute Charge = ₹", round(compute_charge, 2))
print("Storage Charge = ₹", round(storage_charge, 2))
print("Support Fee = ₹", support_fee)
print("Total Bill = ₹", round(total_bill, 2))