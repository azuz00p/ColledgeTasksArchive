# ///////////////////////////////////////////////////////////////////////////////////////
# 17.11
def welcome():
    print("Добро пожаловать!")
    print("Так, сколько там строчек надо?")
    print("А, три? Тогда достаточно.")

def greet(name):
    print(f"Привет, {name}!")

def square(number):
    print(number ** 2)

def rectangle_area(w, h):
    print(w * h)

def convert_minutes(minutes):
    print(f"{minutes // 60} ч {minutes % 60} мин" if minutes > 60 else f"{minutes} мин")

# ///////////////////////////////////////////////////////////////////////////////////////
# 19.11
def double(number):
    return number * 2

def average(a, b, c):
    return (a * b * c) / 3

def is_even(number):
    return True if number % 2 == 0 else False

def max_of_two(a, b):
    return a if a > b else b

def to_minutes(hours, minutes):
    print(f"{hours * 60 + minutes} мин")
