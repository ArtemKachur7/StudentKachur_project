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

def day_of_year(year, month, day):
    if 1 <= month <= 12: #Перевіряємо чи є сенс даних про місяць
        numb_days_in_month = days_in_month(year, month)

        if numb_days_in_month is not None and 1 <= day <= numb_days_in_month: #Перевіряємо чи є сенс даних про кількість днів

            numb_days_in_month = sum(days_in_month(year, m) for m in range(1, month)) + day # Визначаємо номер дня року
            return numb_days_in_month
        else:
            return None
    else:
        return None


print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 13, 31))
print(day_of_year(3000, 11, 30))
print(day_of_year(-2, 13, 31))