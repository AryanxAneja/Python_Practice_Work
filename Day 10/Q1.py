# Write the factorial of a given Number.
num = int(input("Enter a number you want to find the factorial of:"))
factorial = 1
for x in range(1,num+1):
    factorial = factorial * x
print(factorial)