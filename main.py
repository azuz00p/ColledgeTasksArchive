from hub import Hub


# Шаблон для расширения
"""
    elif day == "00.00":
        Hub.H0000(day)
"""

Hub.welcom()
while True:
    print("______________________________________________________")
    day = input("Введите дату урока(-ов)(дд.мм), 0 для выключения: ")
    if day == "0":
        print("Завершение работы...")
        break

    if day == "24.09":
        Hub.H2409(day)

    elif day == "25.09":
        Hub.H2509(day)

    elif day == "29.09":
        Hub.H2909(day)

    elif day == "02.10":
        Hub.H0210(day)

    elif day == "05.10":
        Hub.H0510(day)

    elif day == "12.10":
        Hub.H1210(day)

    elif day == "16.10":
        Hub.H1610(day)

    elif day == "19.10":
        Hub.H1910(day)

    elif day == "21.10":
        Hub.H2110(day)

    elif day == "23.10":
        Hub.H2310(day)

    elif day == "27.10":
        Hub.H2710(day)

    elif day == "28.10":
        Hub.H2810(day)

    elif day == "30.10":
        Hub.H3010(day)

    elif day == "02.11":
        Hub.H0211(day)

    elif day == "06.11":
        Hub.H0611(day)

    elif day == "16.11":
        Hub.H1611(day)

    elif day == "17.11":
        Hub.H1711(day)

    else:
        print("Некорректный ввод")
