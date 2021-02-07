"""
new_dict = {new_key:new_value for item in list if test}

new_dict = {new_key:new_value for (key, value) in dict.items() if test}
"""
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {
    name: random.randint(0, 100) for name in names
}

print(students_score)


passed_students = {
    name: score for (name, score) in students_score.items() if score > 75
}

print(passed_students)


# Excercise 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {
    word: len(word) for word in sentence.split()
}

print(result)

# Excercise 2

weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

temp_f = {
    day: temp * 9/5 + 32 for (day, temp) in weather.items()
}

print(temp_f)

# Pandas DataFrames

student_dict = {
    "student": ["Alex", "James", "Angela", "Lily"],
    "score": [56, 76, 98, 50]
}

print("Regular for loop")
for (key, value) in student_dict.items():
    print(value)

print("With pandas loop")
student_df = pandas.DataFrame(student_dict)

for (key, value) in student_df.items():
    print(value)

print("Pandas iterrows()")
for (index, row) in student_df.iterrows():
    print(row)
