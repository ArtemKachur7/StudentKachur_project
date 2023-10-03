secret_number = 777 #Секретний номер

secret_number_from_user = int(input(""" 
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")) #Номер від користувача

while True: #Створюємо безкінечний  цикл
    if secret_number==secret_number_from_user: #Умова при якій користувач вгадав номер
        print("""╰(▔∀▔)╯Well done,muggle!╰(▔∀▔)╯
              ʕ ᵔᴥᵔ ʔNow you are freedom.ʕ ᵔᴥᵔ ʔ
              """)
        break #Обриваємо цикл
    else: #Умова при якій користувач не вгадав номер
        print("""(＠＾◡＾)Ha-ha!(＠＾◡＾)
        ~You stuck in my loop!~
        """)
        secret_number_from_user = int(input("""
+================================+
| Try again.                |
| So, what is the secret number? |
 +================================+
""")) #Повторний запит на введення числа



