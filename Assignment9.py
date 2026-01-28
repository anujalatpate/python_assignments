# Que 1

def Display():
    print("Jay Ganesh")

Display()

# Que 2
def chkGreater(a, b):
    if a > b:
        print("10 is greater")
    else:
        print("20 is greater")

chkGreater(10, 20)

# Que 3
num = 5
square = num * num
print("Square of number is : ", square)

# Que 4
number = int(input("Enter a number : "))
Cube = number ** 3
print("Cube of number is : ", Cube)

# Que 5
value = int(input("Enter a number :"))


if (value % 3 == 0 and value % 5 == 0):
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")