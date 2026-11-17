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