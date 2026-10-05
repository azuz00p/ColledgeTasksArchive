import hub


# Шаблон для расширения
"""
    elif day == "00.00":
        hub.Hub.H0000(day)
"""

hub.Hub.welcom()
while True:
    print("______________________________________________________")
    day = input("Введите дату урока(-ов)(дд.мм), 0 для выключения: ")
    if day == "0":
        print("Завершение работы...")
        break

    if day == "24.09":
        hub.Hub.H2409(day)

    elif day == "25.09":
        hub.Hub.H2509(day)

    elif day == "29.09":
        hub.Hub.H2909(day)

    elif day == "02.10":
        hub.Hub.H0210(day)

    elif day == "05.10":
        hub.Hub.H0510(day)

    else:
        print("Некорректный ввод")
