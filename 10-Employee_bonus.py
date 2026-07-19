rating = int(input("Enter Employee Rating: "))
experience = int(input("Enter Years of Experience: "))
project_status = input("Enter Project Delivery Status (on time/delayed): ").lower()

if rating == 5 and experience > 10 and project_status == "on time":
    bonus = 30
    print("Bonus Awarded:", bonus, "%")

elif rating == 4 and experience > 7 and project_status == "on time":
    bonus = 20
    print("Bonus Awarded:", bonus, "%")

elif rating == 3 and project_status == "delayed":
    bonus = 5
    print("Bonus Awarded:", bonus, "%")

else:
    print("No Bonus Awarded.")