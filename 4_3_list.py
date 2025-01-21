students = ["dogyeom", "blabla", "maru"]
grades = [2, 1, 4]

print(students[1])
# print(len(students))
# print(len(students[0]))

print ("min(grades)",min(grades))
print ("max(grades)",max(grades))

import statistics
print(statistics.mean(grades))

import random
print("random.choice(students)", random.choice(students))