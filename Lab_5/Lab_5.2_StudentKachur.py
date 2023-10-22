n=int(input("Введіть кілкьість елементів масиву: "))#Введення кількості елементів масива
my_list = []
for i in range(n): #Введення  елементів масива
    elements_mylist = int(input(f"Введіть {i+1}-й елемент масиву: "))
    my_list.append(elements_mylist)
print("Отриманий масив: ",my_list) #Виводимо початковий масив
new_list=[] #Новий пустий масив
for n in my_list:
        if n not in new_list: #Умова при якій числа у новому масиві не будуть повторюватися
            new_list.append(n)
print("The list with unique elements only:")#Виводимо новий масив у якому числа не повторюються
print(new_list)