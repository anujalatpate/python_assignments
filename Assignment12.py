# Que 1
character = "a"
if (character == "a" or character == "e" or character == "i" or character == "o" or character == "u"):
    print("character is a vowel")

else:
    print("character is a consonant")

# Que 2
num = 12
for i in range(1, num+1):
    if num % i ==0:
        print(i, end=" ")

print()

# Que 3
No1 = input("Enter first number : ")
No2 = input("Enter second number : ")

Addition = int(No1) + int(No2)
print("Addition is : ", Addition)

Substraction = int(No1) - int(No2)
print("Substraction is : ", Substraction)

Multiplication = int(No1) * int(No2)
print("Multiplication is : ", Multiplication)

Division = int(No1) / int(No2)
print("Division is : ", Division)

# Que 4
num = 10
for i in range(1, num+1):
    print(i, end=" ")
print()

# Que 5
num = 5
for i in range(num, 0, -1):
    print(i, end=" ")
print()