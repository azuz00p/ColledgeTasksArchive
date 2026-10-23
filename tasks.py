# Шаблон для расширения
"""
class T0000():
    def task1():
        print()

    def task2():
        print()

    def task3():
        print()
""" 

class T2409():
    def task1(name):
        print(f"Привет, {name}! Я - нейросеть ARIA.", f"Инициализация диалога с пользователем {name} завершена.", sep="\n")

    def task2(num1, num2, num3, num4):
        print(f"{num1}.{num2}.{num3}.{num4}", f"{num1}.{num2}.{num3}.{num4}:8080", sep="\n")

    def task3():
        print(*[" [O_O]", "/|___|\\", " |   |", "_|   |_", "RoboHelper v1.0"], sep="\n")

class T2509():
    def task1(num1, num2):
        print(num1 + num2, num1 * num2, sep="\n")

    def task2(num1=1, num2=2):
        print(f"{num1 // num2}\n{num1 % num2}")

    def task3(x, y, n):
        print(f"{n} пирожков будет стоить {x * n + (y * n) // 100} рублей и {y * n % 100} копеек")

    def task4(num):
        print(num // 100 + num % 100 // 10 + num % 10)

    def task5(num):
        print(f"{"Положительное" if num > 0 else "Ноль"}" if num >= 0 else "Отрицательное")

class T2909():
    def task1(num):
        print(f"{"Положительное" if num > 0 else "Ноль"}" if num >= 0 else "Отрицательное", "чётное" if num % 2 == 0 else "нечётное", sep=", ")

    def task2(cost, card):
        print(f"К оплате: {cost * (float(f"{0.9 if cost >= 10000 else 0.95}") if cost >= 5000 else 0) - (0.03 if card.lower() == "да" else 0)}")

class T0210():
    def task1(weather, temp):
        print("Остаёмся дома" if weather.lower() == "дождь" else f"{"Можно идти на пляж" if weather.lower() == "солнце" and temp > 25 else f"{"Идём гулять в парк" if weather.lower() == "солнце" and temp >= 15 else "Читаем книгу дома"}"}")

class T0510():
    def task1(name="user", subscription=True, code=False, VIP=True):
        print("Просмотр разрешён" if name == "user" and (subscription == True or code == True) and VIP else "Нужно оплатить")

    def task2(steps, workout_length, eco_mode):
        print("Поздравить" if (steps >= 10000 or workout_length > 45) and not eco_mode else "Не включать анимацию")

    def task3(n):
        print("*" * n for i in range(n))

    def task4(n):   
        print(*[f'{f"{i + 1}, " if i + 1 < n else i}' if i % 2 != 0 else "" for i in range(n)][:-2], sep="", end=f"{n if n % 2 == 0 else n - 1}\n")

class T1210():
    def task1(n):
        while n >= 0:
            print(n)
            n -= 1

class T1610():
    def task1(n):
        while True:
            if n == 0:
                break
            print(n)
            n = int(input())

    def task2():
        while True:
            n = input("Введите положительное число: ")
            try:
                if int(n) > 0:
                    break      
            except:
                print("Ошибка: Введено не число")

    def task3(n):
        list = []
        for i in range(n, 1, -5):
            if i % 2 == 0:
                continue
            list.append(i)
            if i < 10:
                print(f"Меньше 10\nВыбранные числа: {list[0]}", *list[1:], sep="; ")
                break

class T1910():
    def task1(line, word):
        print(line.find(word) if word in line else "Не найдено")

    def task2(phrase):
        print(phrase.replace(" ", "_"))

    def task3(line, symbol):
        print(f"Первое: {line.find(symbol)}, последнее: {line.rfind(symbol)}." if symbol in line else "Не найдено")

class T2110():
    def task1(n, line):
        print(line.upper() if n == "1" else ("Принято" if line.lower() == "да" else "Отклонено") if n == "2" else line.capitalize() if n == "3" else line.swapcase() if n == "4" else line.strip() if n == "5" else line.lstrip() if n == "6" else line.rstrip() if n == "7" else "Некорректное число")

class T2310():
    def task1(n):
        print([4] * n)
