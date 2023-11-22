def numbers_in_range(request, min_value, max_value): #Функція для перевірки чи лежать цілі числа у певному діапазоні
    while True:
        try: #Випадок коли число  лежить у діапазоні
            user_input = int(input(request))

            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})") #Випадок коли число не лежить у діапазоні
        except ValueError: #Виняток коли ви ввели не вірне значення
            print("Error: Wrong input! Please enter an integer.")

#Тестуємо функцію
min_value = int(input("Min Value: "))
max_value = int(input("Max Value: "))
result = numbers_in_range(f"Enter an integer between {min_value} and {max_value}: ", min_value, max_value)
print(f"You entered: {result}")