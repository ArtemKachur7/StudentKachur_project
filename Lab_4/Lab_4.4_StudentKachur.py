numb_year = int(input("Введіть рік (наприклад,2004): "))#Вводимо рік
if numb_year%4!=0: #Умова при якій не ділиться на 4 — звичайний рік
    if numb_year < 1582: #Додаткова умова при якій рік не належить Григоріанському календарю
        print("Not within the Gregorian calendar period.")
    else:
        print("Common year")
elif numb_year%100!=0 : #Умова при якій не ділиться на 100 — високосний рік
    if numb_year < 1582: #Додаткова умова при якій рік не належить Григоріанському календарю
        print("Not within the Gregorian calendar period.")
    else:
        print("Leep year")
elif numb_year % 400!=0 : #Умова при якій не ділиться на 400 — звичайний рік
    if numb_year < 1582: #Додаткова умова при якій рік не належить Григоріанському календарю
        print("Not within the Gregorian calendar period.")
    else:
        print("Common year")
else: #Якщо жодна з умов не виконується — високосний рік
    if numb_year < 1582: #Додаткова умова при якій рік не належить Григоріанському календарю
        print("Not within the Gregorian calendar period.")
    else:
        print("Leep year")