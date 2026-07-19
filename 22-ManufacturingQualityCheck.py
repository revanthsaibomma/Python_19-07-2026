# 13. Manufacturing Quality Check
# Input:
# •	defect count
# •	machine temperature
# •	production speed
# •	operator experience
# Rules:
# •	Reject batch if defects exceed limit
# •	If machine temperature is too high and speed is high → Risk
# •	If operator experience low and defect rising → Warning
# •	Else accept batch

defect_count = int(input("Enter Defect Count: "))
temperature = float(input("Enter Machine Temperature (°C): "))
speed = float(input("Enter Production Speed (units/hour): "))
experience = int(input("Enter Operator Experience (years): "))

if defect_count > 10:
    print("Batch Status : Rejected")
    print("Reason : Defect count exceeds the acceptable limit.")

elif temperature > 80 and speed > 100:
    print("Batch Status : Risk")
    print("Reason : High machine temperature and high production speed.")

elif experience < 2 and defect_count > 5:
    print("Batch Status : Warning")
    print("Reason : Operator has low experience and defects are increasing.")

else:
    print("Batch Status : Accepted")
    print("Reason : Batch meets the quality standards.")