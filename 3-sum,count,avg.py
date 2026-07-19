sub1 = int(input("Enter the marks of subject 1: "))
sub2 = int(input("Enter the marks of subject 2: "))
sub3 = int(input("Enter the marks of subject 3: "))
sub4 = int(input("Enter the marks of subject 4: "))
sub5 = int(input("Enter the marks of subject 5: "))

sum = sub1 + sub2 + sub3 + sub4 + sub5
count = len([sub1, sub2, sub3, sub4, sub5])
average = sum / count

print("The total marks are:", sum)
print(f"The total marks are: {sum}")
print(sum)
print("The average marks are:", average)
print(f"The average marks are: {average}")
print(average)
print("The number of subjects are:", count)
print(f"The number of subjects are: {count}")
print(count)