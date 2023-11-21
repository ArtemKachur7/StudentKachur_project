def is_a_triangle(a, b, c): #Функція , яка перевіряє чи можливо створити трикутник зі сторін заданої довжини
    if a <= 0 or b<= 0 or c <= 0 :
        return None
    else:
        return a + b > c and b + c > a and c + a > b
def is_a_right_triangle(a, b, c): #Функція , яка перевіряє чи трикутник прямокутний
    if not is_a_triangle(a, b, c):
        return None
    side = sorted([a, b, c])
    return side[0]**2 + side[1]**2 == side[2]**2

#тестуючий код
a = int(input("Введіть довжину сторони а: "))
b = int(input("Введіть довжину сторони b: "))
c = int(input("Введіть довжину сторони c: "))

result = is_a_right_triangle(a, b, c)

if result is None:
    print(f"Трикутник із сторонами а={a}, b={b}, c={c} - не є прямокутним або не є трикутником.(Сторони трикутника повинні бути більше 0!)")
elif result:
    print(f"Трикутник із сторонами а={a}, b={b}, c={c} - є прямокутним.")
