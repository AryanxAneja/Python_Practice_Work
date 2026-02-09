# WAP to find a substring within a string and print the number of times the substring occurs. String traversal takes place from left to right
string = input("Enter main string: ")
sub = input("Enter substring: ")

count = 0
n = len(string)
m = len(sub)

for i in range(n - m + 1):
    if string[i:i+m] == sub:
        count += 1

print("Substring occurs", count, "times")
