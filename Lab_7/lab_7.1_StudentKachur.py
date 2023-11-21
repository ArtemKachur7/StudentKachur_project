str_tuple1=input("Введіть перший рядок: ") #Вводимо кожен рядок
str_tuple2=input("Введіть другий рядок: ")
str_tuple3=input("Введіть третій рядок: ")

strings_tuple = (str_tuple1, str_tuple2, str_tuple3) #Створюємо кортеж з трьох рядків

result = ', '.join(strings_tuple) #З'єднануємо 3 рядки через кому

print("З'єднаний рядок:", result)