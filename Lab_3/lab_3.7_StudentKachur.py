hour = int(input("Starting time (hours): ")) #Водимо годину , о котрій почалась подія
mins = int(input("Starting time (minutes): ")) #Водимо хвилину , о котрій почалась подія
dura = int(input("Event duration (minutes): ")) #Водимо кількість хвилин , які пройшли з кінця і до початку події
all_mins = hour*60 + mins + dura #Рахуємо скільки всього хвилин разом у трьох нащих змінних
max_hours = (all_mins//60)%24 #Створюємо формулу для максимального заповнення годин часу
max_mins = all_mins%60 #Створюємо формулу для максимального заповнення хвилин часу
print("Expected result: ",max_hours,":",max_mins) #Виводимо результат
