# Que 1
lengthOfRectangle = input("Enter length: ")
width = input("Enter width: ")
area = int(lengthOfRectangle) * int(width)
print("The area of the rectangle is:", area)

# Que 2
radious = input("Enter radious : ")
pi = 3.14
areaOfCircle = pi * (int(radious) ** 2)
print("The area of the circle is:", areaOfCircle)

# Que 3
num = 6
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("this is a perfect number")
else:
    print("this is Not a perfect number")

# Que 4
num = int(input("Enter a number: "))
print("Binary equivalent:", bin(num)[2:])

# Que 5
marks = int(input("Enter a number: "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 50:
    print("Second Class")
else:
    print("Fail")

