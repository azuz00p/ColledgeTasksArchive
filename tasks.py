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
