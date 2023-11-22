def calculate_life_number(date):
    # Видалення всіх символів, окрім цифр
    digits = ''.join(filter(str.isdigit, date))

    if not digits: # Якщо не залишилося жодної цифри, викликаємо виняток
        raise ValueError("Введена дата не містить цифр.")

    # Вирахування суми цифр
    digit_sum = sum(int(d) for d in digits)

    # Повторне додавання, якщо результат містить більше однієї цифри
    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))

    return digit_sum


while True:
    try: # Обчислення цифри життя та виведення результату
        # Запит дати народження користувача
        date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")
        life_number = calculate_life_number(date)
        print("Цифра життя для дати {}: {}".format(date, life_number))
        break
    except ValueError as e:
        print(f"Помилка!Некоректне введення. {e}")

