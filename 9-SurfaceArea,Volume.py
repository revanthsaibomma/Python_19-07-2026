import math

print("Choose Solid Shape")
print("1. Cube")
print("2. Cylinder")
print("3. Cone")
print("4. Cuboid")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter the side of the cube: "))

    surface_area = 6 * side ** 2
    volume = side ** 3

    print("\nSurface Area of Cube =", surface_area)
    print("Volume of Cube =", volume)

elif choice == 2:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius ** 2 * height

    print("\nSurface Area of Cylinder =", round(surface_area, 2))
    print("Volume of Cylinder =", round(volume, 2))

elif choice == 3:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))

    slant_height = math.sqrt(radius ** 2 + height ** 2)
    surface_area = math.pi * radius * (radius + slant_height)
    volume = (1/3) * math.pi * radius ** 2 * height

    print("\nSurface Area of Cone =", round(surface_area, 2))
    print("Volume of Cone =", round(volume, 2))

elif choice == 4:
    length = float(input("Enter the length of the cuboid: "))
    breadth = float(input("Enter the breadth of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))

    surface_area = 2 * (length * breadth + breadth * height + height * length)
    volume = length * breadth * height

    print("\nSurface Area of Cuboid =", surface_area)
    print("Volume of Cuboid =", volume)

else:
    print("Invalid Choice")