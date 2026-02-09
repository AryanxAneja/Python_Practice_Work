# To find the greatest among the three numbers, assuming no two numbers are same.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest number is:", a)
elif b > a and b > c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)