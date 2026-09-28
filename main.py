import hub


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
        hub.Hub.H2509

    else:
        print("Некорректный ввод")
