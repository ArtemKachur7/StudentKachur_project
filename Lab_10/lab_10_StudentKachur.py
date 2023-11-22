def game_words_combination(word, combination):
    word = word.lower() # Перетворюємо обидва рядки в нижній регістр для ігнорування чутливості до регістру
    combination = combination.lower()
    start_index = 0

    for char in word:  # Перевіряємо кожен символ слова в комбінації за допомогою функції find()
        index = combination.find(char,start_index)

        if index == -1: #Варіант коли символ не знайдено
            return "No"


        combination = combination[index + 1:]# Після знаходження необхідного символа, відсікаємо вже перевірений фрагмент комбінації


    return "Yes" # Варіант коли всі символи знайдено


#Тестуємо функцію
word_user = input("Введіть ваше слово: ")
combination_user = input("Введіть вашу комбінацію : ")

result = game_words_combination(word_user, combination_user)
print(result)

