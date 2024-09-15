#program for surface area of a cylinder
r = int (input("Enter the radius: "))
h= int (input("Enter the height: "))
sa = 2 * 3.142 * r**2 + 2 * 3.142 * r * h
print("The surface area is: " , sa)
print(type (sa))