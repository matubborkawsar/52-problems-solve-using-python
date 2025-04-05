number = int(input("Enter a number : "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

zero = 0

while factorial % 10 == 0:
    zero += 1
    factorial //= 10

print(zero)