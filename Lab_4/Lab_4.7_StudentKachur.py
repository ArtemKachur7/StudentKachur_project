secret_word = "chupacabra" #Секретне слово
secret_word_from_user = input("What is the secret word? ") #Секретне слово від користувача
while True: #Безкінечний цикл
    if secret_word_from_user==secret_word: #Умова при якій слово вгадали
        print("You are true!")
    else:
        print("You've successfully left the loop.")#Умова при якій слово не вгадали
        break #Закінчення циклу