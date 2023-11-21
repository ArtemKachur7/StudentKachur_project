def is_a_triangle(a, b, c): #Функція , яка перевіряє чи можливо створити трикутник зі сторін заданої довжини
    if a <= 0 or b<= 0 or c <= 0 :
        return None
    else:
        return a + b > c and b + c > a and c + a > b

#тестуючий код
a = int(input("Введіть довжину сторони а: "))
b = int(input("Введіть довжину сторони b: "))
c = int(input("Введіть довжину сторони c: "))
result = is_a_triangle(a, b, c)
if result is not None:
    if result:
        print(f"Сторони a={a}, b={b}, c={c} - можуть утворити трикутник.")
    else:
        print(f"Сторони a={a}, b={b}, c={c} - не можуть утворити трикутник.")
else:
    print("Помилка!Довжина сторони повинна бути більша за нуль!")