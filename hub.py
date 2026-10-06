import tasks


# Шаблон для расширения
"""
    def H0000(day):
            while True:
                print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
                task = input("Введите номер задания(1-3, 0 для возвращения): ")
                if task == "0":
                    print("Возвращение к выбору даты...")
                    break
                elif task == "1":
                    ...
                elif task == "2":
                    ...
                elif task == "3":
                    ...
                else:
                    print("Некорректный ввод")
"""

class Hub():
    def welcom():
        print("______________________________________________________",
            *["__        __  _____   _        ____    ___    __  __   _____ ",
            "\\ \\      / / | ____| | |      / ___|  / _ \\  |  \\/  | | ____|",
            " \\ \\ /\\ / /  |  _|   | |     | |     | | | | | |\\/| | |  _|",
            "  \\ V  V /   | |___  | |___  | |___  | |_| | | |  | | | |___ ",
            "   \\_/\\_/    |_____| |_____|  \\____|  \\___/  |_|  |_| |_____|"], sep="\n")
        
    def H2409(day):
        while True:
            print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
            task = input("Введите номер задания(1-3, 0 для возвращения): ")
            if task == "0":
                print("Возвращение к выбору даты...")
                break
            elif task == "1":
                tasks.T2409.task1(input())
            elif task == "2":
                tasks.T2409.task2(int(input()), int(input()), int(input()), int(input()))
            elif task == "3":
                tasks.T2409.task3()
            else:
                print("Некорректный ввод")

    def H2509(day):
        while True:
            print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
            task = input("Введите номер задания(1-5, 0 для возвращения): ")
            if task == "0":
                print("Возвращение к выбору даты...")
                break
            elif task == "1":
                tasks.T2509.task1(int(input()), int(input()))
            elif task == "2":
                if input("Хотите вставить свои числа? (Y/N) ").upper() == "Y":
                    tasks.T2509.task2(int(input()), int(input()))
                else:
                    tasks.T2509.task2()
            elif task == "3":
                tasks.T2509.task3(int(input("Введите стоимость(рубли): ")), int(input("Введите стоимость(копейки): ")), int(input("Введите количество: ")))
            elif task == "4":
                tasks.T2509.task4(int(input("Введите трёхзначное число: ")))
            elif task == "5":
                tasks.T2509.task5(int(input("Введите число: ")))
            else:
                print("Некорректный ввод")

    def H2909(day):
            while True:
                print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
                task = input("Введите номер задания(1-2, 0 для возвращения): ")
                if task == "0":
                    print("Возвращение к выбору даты...")
                    break
                elif task == "1":
                    tasks.T2909.task1(int(input()))
                elif task == "2":
                    tasks.T2909.task2(int(input()), input())
                else:
                    print("Некорректный ввод")

    def H0210(day):
            while True:
                print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
                task = input("Введите номер задания(1, 0 для возвращения): ")
                if task == "0":
                    print("Возвращение к выбору даты...")
                    break
                elif task == "1":
                    tasks.T0210.task1(input(), int(input()))
                else:
                    print("Некорректный ввод")

    def H0510(day):
            while True:
                print("______________________________________________________", f"Выбрана дата: {day}", sep="\n")
                task = input("Введите номер задания(1-4, 0 для возвращения): ")
                if task == "0":
                    print("Возвращение к выбору даты...")
                    break
                elif task == "1":
                    if input("Хотите ввести свои данные? (Y/N)").upper() == "Y":
                        tasks.T0510.task1(input(), True if input().lower() in ["true", "yes", "да"] else False, True if input().lower() in ["true", "yes", "да"] else False, True if input().lower() in ["true", "yes", "да"] else False)
                    else:
                        tasks.T0510.task1()
                elif task == "2":
                    tasks.T0510.task2(int(input()), int(input()), True if input().lower() in ["true", "yes", "да"] else False)
                elif task == "3":
                    tasks.T0510.task3(int(input()))
                elif task == "4":
                    tasks.T0510.task4(int(input()))
                else:
                    print("Некорректный ввод")
