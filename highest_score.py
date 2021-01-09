students_score = input("Enter a list of student scores: ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)

hight_score = 0

for i in students_score:
    if i > hight_score:
        hight_score = i
print(f"The highest score is: {hight_score}")
