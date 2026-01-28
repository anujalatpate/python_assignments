from functools import reduce

# Que 1
Data = list(map(int, (input("Enter number : ").split())))
squares = lambda No: No * No

MapData = list(map(squares, Data))
print("Square of numbers are : ", MapData)

# Que 2
Data = list(map(int, (input("Enter number : ").split())))
print(Data)
checkEven = lambda No : (No % 2 == 0)
FilterData = list(filter(checkEven, Data))
print("Even numbers are : ", FilterData)

# Que 3
Data = list(map(int, (input("Enter numbers : ").split())))
print(Data)
checkOdd = lambda No: (No % 2 != 0)
filterOdd = list(filter(checkOdd, Data))
print("Odd numbers are : ", filterOdd)

# Que 4
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
Addition = lambda a, b : a + b
Result = reduce(Addition, Data)
print("Addition of numbers is : ", Result)

# Que 5
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
Maximum = lambda No1, No2 : No1 if No1 > No2 else No2
Result = reduce(Maximum, Data)
print("Maximum number is : ", Result)

# Que 6
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
Minimum = lambda No1, No2 : No1 if No1 < No2 else No2
Result = reduce(Minimum, Data)
print("Minimum number is : ", Result)

# Que 7
Data = list(input("Enter names : ").split())
print(Data)
Names = lambda value: len(value) > 5
filterNames = list(filter(Names, Data))
print(filterNames)

# Que 8
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
Output = lambda No: (No % 3 == 0) and (No % 5 == 0)
filterDivisible = list(filter(Output, Data))
print("Divisible by 3 and 5 numbers are : ", filterDivisible)

# Que 9
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
Multiplication = lambda No1, No2: No1 * No2
Result = reduce(Multiplication, Data)
print(Result)

# Que 10
Data = list(map(int, input("Enter numbers : ").split()))
print(Data)
filterEvenCount = lambda No: (No % 2 == 0)
Result = list(filter(filterEvenCount, Data))
print("Even number counts is : " , len(Result))