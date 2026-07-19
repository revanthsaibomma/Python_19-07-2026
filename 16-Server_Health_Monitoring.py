# 7. Server Health Monitoring Decision
# Input:
# •	CPU usage
# •	memory usage
# •	disk usage
# •	network latency
# Rules:
# •	If CPU > 90 and memory > 85 → Critical alert
# •	If disk > 95 → Storage critical
# •	If latency > threshold → Network issue
# •	Else classify as healthy / warning / critical

cpu = float(input("Enter CPU Usage (%): "))
memory = float(input("Enter Memory Usage (%): "))
disk = float(input("Enter Disk Usage (%): "))
latency = float(input("Enter Network Latency (ms): "))

if cpu > 90 and memory > 85:
    print("Status : Critical Alert")
    print("Reason : CPU and Memory usage are very high.")

elif disk > 95:
    print("Status : Storage Critical")
    print("Reason : Disk usage exceeded safe limit.")

elif latency > 100:
    print("Status : Network Issue")
    print("Reason : Network latency is too high.")

elif cpu > 70 or memory > 70 or disk > 80:
    print("Status : Warning")
    print("Reason : Resource usage is above normal.")

else:
    print("Status : Healthy")
    print("Reason : All server resources are operating normally.")