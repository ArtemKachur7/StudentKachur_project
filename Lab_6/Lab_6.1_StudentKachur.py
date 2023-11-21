def is_year_leap(year): #Функція на перевірку чи високосний рік , якщо він високосний він без залишку ділиться на 4 , 100 або 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month): #Функція для визначення кількості днів у місяці

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#список із зазначенням дожвини місяця

    if is_year_leap(year): #Якщо рік високосний у Лютому 29 днів
        days_in_month[1] = 29

    if 1 <= month <= 12: #Перевіряємо чи мають аргументи функціїї сенс , якщо ні — повертаємо None
        return days_in_month[month - 1]
    else:
        return None

#тестуючий код
test_years = [1900, 2000, 2016, 1987,2024,3000,2004]
test_months = [2, 2, 1, 11,11,46 , 14]
test_results = [28, 29, 31,30,30,200 ,30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")