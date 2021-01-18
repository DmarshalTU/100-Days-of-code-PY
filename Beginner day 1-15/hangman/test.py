import functools

# map:
def square(num):
    return num ** 2

list_of_numbers = [2, 3, 4, 5, 6]

result = map(square, list_of_numbers)
print(list(result))

# filter:

my_files = ['qqq.mp3', 'ewq.docx', 'das.pdf', 'fdc.mp3']

def is_mp3_file(filename):
    return filename.endswith('.mp3')

print(list(filter(is_mp3_file, my_files)))

def func(x):
    return x % 2 != 0

print(list(filter(func, range(10))))

# reduce:

def add(a, b):
    return a + b

shopping_list = [1, 2, 3, 4, 5]

print(functools.reduce(add, shopping_list))
print(functools.reduce(lambda x, y : x + y, shopping_list))


def secret(a):
    return a % 3 != 0 and a % 5 != 0
result = filter(secret, range(1, 31))
print(list(result))




# def combine_coins(a, b):
#     return a * b
# print(combine_coins('$', range(5))) 