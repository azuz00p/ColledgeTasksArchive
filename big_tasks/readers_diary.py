def diary(lst=[]):
    while True:
        n = input("""   === ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===
    1 - Добавить книгу
    2 - Показать все книги
    3 - Показать последние 5 прочитанных
    4 - Заменить название по номеру
    5 - Поиск по названию
    6 - Статистика
    7 - Удалить книгу
    0 - Выход
""")

        if n == "1":
            title = input().strip()
            if title != "":
                lst.append(f"{len(lst) + 1}. {title}")
                print("Книга успешно добавлена")
            else:
                print("Ошибка: пустая строка / строка из пробелов")

        elif n == "2":
            print(*lst, sep="\n")

        elif n == "3":
            if len(lst) > 5:
                    print(*lst[-5:], sep="\n")
            else:
                print(*lst, sep="\n")

        elif n == "4":
            try:
                e, title = int(input("Выберите номер: ")), input().strip()
                if title != "":
                    lst[e - 1] = f"{e}. {title}"
                else:
                    print("Ошибка: пустая строка / строка из пробелов")
            except IndexError:
                print("Ошибка: недействительный номер книги")
                

        elif n == "5":
            line = input("Поиск: ")
            for elem in lst:
                if line.lower() in elem.lower():
                    print(elem)
                    break
            if line not in lst[-1]:
                print("Ничего не найдено")

        elif n == "6":
            print(f"Всего книг: {len(lst)}", lst[0], lst[-1], sep="\n")

        elif n == "0":
            break

        else:
            print("Ошибка: некорректный ввод")