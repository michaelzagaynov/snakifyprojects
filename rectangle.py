print("What's your name?")
n=input()
print("Hi " + str(n) + "!" + " How tall do you want your pool to be?")
height=input()
print("how wide do you want your pool to be?")
width = input()
print("how long do you want your pool to be?")
length=input()
rectangle = int(width)*int(height)*int(length) * 7.5
square = int(width) * int(width) * int(height) * 7.5
circle = 3.14 * (int(width)/2) ** 2 * int(height) * 5.875
print("So, " + str(n) + ", a rectangular pool those dimensions would be" + str(rectangle) + " gallons, ")
print("a square pool those dimensions would be" + str(square) + "gallons")
print("and a spherical pool those dimensions would be" + str(circle) + "gallons")