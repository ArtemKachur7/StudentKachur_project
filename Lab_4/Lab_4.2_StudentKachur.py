spathiphyllum = input("Write the best plant ever: ") #Вводимо назву рослини
if spathiphyllum == "spathiphyllum":    #Задаємо умови виводу:1) Якщо лілія введено з маленької літери
    print("No, I want a big Spathiphyllum!")
elif spathiphyllum == "Spathiphyllum": #2) Якщо лілія введено з великої літери
    print("Yes - Spathiphyllum is the best plant ever!")
else:
    print(f"Spathiphyllum! Not {spathiphyllum}!") #3) Якщо введено зовісм іншу рослину
