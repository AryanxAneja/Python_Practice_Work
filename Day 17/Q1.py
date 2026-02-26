# Problem: You are given three groups of students and their hobby sets.
# Write a Python program using set operations to find:
# 1. Hobbies enjoyed by all three students
# 2. Hobbies enjoyed by at least two students (but not necessarily all three)
# 3. Hobbies that only one student enjoys (unique to them)
# 4. All hobbies across all three students combined

student1 = {"reading", "gaming", "cooking", "cycling"}
student2 = {"gaming", "cooking", "painting", "hiking"}
student3 = {"cooking", "cycling", "hiking", "reading"}

common_all = student1 & student2 & student3

at_least_two = (student1 & student2) | (student1 & student3) | (student2 & student3)

unique_student1 = student1 - student2 - student3
unique_student2 = student2 - student1 - student3
unique_student3 = student3 - student1 - student2

all_hobbies = student1 | student2 | student3

print("Common to all three:", common_all)
print("Enjoyed by at least two:", at_least_two)
print("Unique to student1:", unique_student1)
print("Unique to student2:", unique_student2)
print("Unique to student3:", unique_student3)
print("All hobbies combined:", all_hobbies)
