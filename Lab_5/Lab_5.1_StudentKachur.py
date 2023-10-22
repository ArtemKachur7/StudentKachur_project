n=int(input("Введіть кілкьість елементів масиву: "))# 1 реалізувати інтерактивне введення елементів масива
my_list = []
for i in range(n):
    elements_mylist = int(input(f"Введіть {i+1}-й елемент масиву: "))
    my_list.append(elements_mylist)
print("Отриманий масив: ",my_list) #Виводимо початковий масив
for bubble in range(n-1): #Метод бульбашки
    for i in range(n-1-bubble):
        if my_list[i]>my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
            swapped = True # 2 оптимізувати процедуру сортування(Якщо елементи не переставлялися — значить масив вже відсортований у порядку зростання)
            if not swapped:
                break
print("Масив відсортований методом бульбашки: ",my_list) #Виводимо відсортований масив