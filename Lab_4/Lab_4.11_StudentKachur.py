c_0 = int(input("Введіть ціле число(не від'ємне): ")) #Вводимо наше число с0
print("Ваше число: ",c_0) #Виводимо наше число с0
steps = 0 #Змінна дял підрахунку кількості ітерацій
while c_0!=1: #Умова до якої працює цикл
   if c_0%2==0: #Перша умова циклу при якій с0 — парне число
       c_0 = c_0//2
       print(c_0)#Виводимо наше число с0 після кожної ітерації
       steps += 1 #Конструкція , яка підраховує кількість ітерація
   elif c_0%2!=0:#Друга умова циклу при якій с0 — непарне число
       c_0 = 3*c_0 + 1
       print(c_0)#Виводимо наше число с0 після кожної ітерації
       steps += 1#Конструкція , яка підраховує кількість ітерація
print("steps = ",steps)#Виводимо кінцеве число ітерацій



