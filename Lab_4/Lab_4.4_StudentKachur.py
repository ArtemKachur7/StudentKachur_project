income = float(input("Enter the annual income: ")) #Вовдимо заробітну плату за рік

if income <= 85528 :   #Вираховуємо податок для зарплати менше або = 85528 талерів
    tax = income/100*18-556.02
    tax = round(tax,0)
    if tax < 0: #Умова за якої податкова ніколи не повертає гроші
        tax = 0.0
    print("The tax is:", tax, "thalers") #Виводимо податок
elif income > 85528  :  #Вираховуємо податок для зарплати більше 85528 талерів
    tax = (income-85528)/100*32+14839.02
    tax = round(tax,0)
    if tax < 0: #Умова за якої податкова ніколи не повертає гроші
        tax = 0.0
    print("The tax is:", tax, "thalers")#Виводимо податок





