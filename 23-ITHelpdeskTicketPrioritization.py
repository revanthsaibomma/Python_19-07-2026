# 14. IT Helpdesk Ticket Prioritization
# Take:
# •	issue severity
# •	department
# •	business impact
# •	VIP user status
# Rules:
# •	Critical severity + VIP user → P1
# •	Critical severity + high business impact → P1
# •	Medium severity → P3
# •	Low severity → P4
# •	Else assign appropriate priority

severity = input("Enter Issue Severity (Critical/Medium/Low): ").lower()
department = input("Enter Department: ")
business_impact = input("Enter Business Impact (High/Medium/Low): ").lower()
vip = input("Is the User a VIP? (yes/no): ").lower()

if severity == "critical" and vip == "yes":
    print("Ticket Priority : P1")
    print("Reason : Critical issue reported by a VIP user.")

elif severity == "critical" and business_impact == "high":
    print("Ticket Priority : P1")
    print("Reason : Critical issue with high business impact.")

elif severity == "medium":
    print("Ticket Priority : P3")
    print("Reason : Medium severity issue.")

elif severity == "low":
    print("Ticket Priority : P4")
    print("Reason : Low severity issue.")

else:
    print("Ticket Priority : P2")
    print("Reason : Moderate priority issue.")