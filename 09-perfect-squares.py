import math

number = int(input("Enter a number: "))

sqr = math.sqrt(number)
if sqr.is_integer():
    print("YES")
else:
    print("NO")