# 12. Data Center Power Usage Classification
# Take:
# •	total power consumption
# •	cooling efficiency
# •	rack load percentage
# Rules:
# •	If power exceeds safe limit and cooling is poor → Critical
# •	If rack load > threshold → Warning
# •	Efficient cooling and balanced load → Normal
# •	Else moderate risk

power = float(input("Enter Total Power Consumption (kW): "))
cooling = float(input("Enter Cooling Efficiency (%): "))
rack_load = float(input("Enter Rack Load Percentage (%): "))

if power > 1000 and cooling < 70:
    print("Status : Critical")
    print("Reason : High power consumption with poor cooling.")

elif rack_load > 85:
    print("Status : Warning")
    print("Reason : Rack load exceeds the safe threshold.")

elif cooling >= 85 and rack_load <= 70:
    print("Status : Normal")
    print("Reason : Efficient cooling and balanced rack load.")

else:
    print("Status : Moderate Risk")
    print("Reason : Power usage requires monitoring.")