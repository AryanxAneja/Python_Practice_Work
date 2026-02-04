# print fibonacci series upto the given term
num = int(input("Enter a Number - "))
def fibonacci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(num))