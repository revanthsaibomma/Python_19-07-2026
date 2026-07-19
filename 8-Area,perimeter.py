import math

print("Choose Shape")
print("1. Square")
print("2. Circle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    side = float(input("Enter the side of the square: "))
    area = side * side
    perimeter = 4 * side

    print(f"\nArea of Square = {area}")
    print(f"Perimeter of Square = {perimeter}")

elif choice == 2:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius

    print(f"\nArea of Circle = {round(area, 2)}")
    print(f"Circumference of Circle = {round(circumference, 2)}")

elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))

    area = 0.5 * base * height
    perimeter = side1 + side2 + side3

    print(f"\nArea of Triangle = {area}")
    print(f"Perimeter of Triangle = {perimeter}")

else:
    print("Invalid Choice")