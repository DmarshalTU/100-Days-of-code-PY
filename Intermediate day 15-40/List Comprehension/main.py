"""
new_list = [new_item for item in items if test]
"""

numbers = [1, 2, 3, 4, 5]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print("Before Comprehension:")
print(f"Old list is: {numbers}")
print(f"New list is: {new_list}")

numbers = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in numbers]

print("After Comprehension:")
print(f"Old list is: {numbers}")
print(f"New list is: {new_list}")

name = "Denis"
list_ = [letter for letter in name]

print(f"Name list: {list_}")


new_range = [_ * 2 for _ in range(1, 5)]
print(f"New doubled range is: {new_range}")

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(f"List of names: {names}")

short_names = [short_name for short_name in names if len(short_name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]

print(f"The names that shorter than 4: {short_names}")
print(f"Upper case names that len > 5: {upper_names}")

# Squared number exercise
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(f"Squared numbers id: {squared_numbers}")

# Filtering even numbers exercise
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Even numbers are: {even_numbers}")

# Data overlap
with open("file1.txt") as file1:
    f1_list = file1.readlines()

with open("file2.txt") as file2:
    f2_list = file2.readlines()

compare_list = [int(number.strip()) for number in f1_list if number in f2_list]
print(f"Compare result: {compare_list}")
