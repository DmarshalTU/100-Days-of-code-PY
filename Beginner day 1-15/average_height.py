students_height = input("Input a list of students heights ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)

summ = 0
for i in students_height:
    summ += i
avrg_h = round(summ / len(students_height))
print(avrg_h)
