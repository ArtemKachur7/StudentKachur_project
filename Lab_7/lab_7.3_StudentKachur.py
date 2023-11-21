students = {}  # Початковий пустий словник

while True: #Створюємо нескінченний цикл для заповнення словника
    last_name = input("Введіть прізвище студента (або Enter, щоб завершити): ")#Вводимо інформацію про студента
    if last_name=="":
        break

    first_name = input("Введіть ім'я студента: ")#Вводимо інформацію про студента
    age = int(input("Введіть вік студента: "))
    facultet = input("Введіть факультет студента: ")
    group = input("Введіть групу студента: ")
    specialnist = input("Введіть спеціальність студента: ")
    score = input("Введіть бали студента через кому (від 0 до 100): ")
    scores_str_list = score.split(',')
    scores = [int(score) for score in scores_str_list if score.strip().isdigit()]# Перетворюємо рядок в список цілих чисел
    new_score = sum(scores) / len(scores)
    students[last_name] = (first_name, age,new_score,facultet, group , specialnist)# Додаємо запис у словник

last_name = input("Введіть прізвище студента данні якого вас цікавлять: ") #Користувач запитує інформацію про студента за прізвищем


if last_name in students: # Перевіряємо, чи існує студент з введеним прізвищем у словнику
    # Виводимо інформацію про студента
    student_info = students[last_name]
    print(f"Ім'я: {student_info[0]}")
    print(f"Вік: {student_info[1]}")
    print(f"Середній бал: {student_info[2]}")
    print(f"Факультет: {student_info[3]} ")
    print(f"Група: {student_info[4]} ")
    print(f"Спеціальність: {student_info[5]}")
else:
    print(f"Студента з прізвищем '{last_name}' не знайдено.")
