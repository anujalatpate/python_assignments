# Que 1
num = int(input("Enter a number : "))
square = lambda num : num * num
print("square of given number is : ", square(num))

# Que 2
num = int(input("Enter a number : "))
cube = lambda num : (num ** 3)
print("cube of given number is : ", cube(num))

# Que 3
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
maximum = lambda No1,No2 : No1 if(No1>No2) else No2
print("Maximum of two numbers is : ", maximum(No1,No2))

# Que 4
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
minimum = lambda No1,No2 : No1 if(No1<No2) else No2
print("Minimum of two numbers is : ", minimum(No1,No2))

# Que 5
num = int(input("Enter a number  : "))
checkEven = lambda num : True if(num % 2 ==0) else False
print(checkEven(num))

# Que 6
num = int(input("Enter a number  : "))
checkOdd = lambda num : True if(num % 2 != 0) else False
print(checkOdd(num))

# Que 7
num = int(input("Enter a number : "))
divisibleBy5 = lambda num : True if (num % 5 == 0 ) else False
print(divisibleBy5(num))

# Que 8
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
Addition = lambda No1,No2 : No1 + No2
print("Addition of two numbers is : ", Addition(No1,No2))

# Que 9
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
Multiplication = lambda No1,No2 : No1 * No2
print("Multiplication of two numbers is : ", Multiplication(No1,No2))

# Que 10
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))
No3 = int(input("Enter third number : "))
largestNumber = lambda No1,No2,No3 : No1 if (No1>No2 and No1>No3) else (No2 if (No2>No3) else No3)
print("Largest numbers is : ", largestNumber(No1,No2,No3))