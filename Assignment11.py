# Que 1
num = 11
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Que 2
num = 7521
print("The digits are:", len(str(num)))

# Que 3
num = 123
sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)
print("The sum of digits is:", sum_of_digits)

# Que 4
num = 123
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10
print("The reversed number is:", reversed_num)

# Que 5
num = 121
value = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10
if value == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")