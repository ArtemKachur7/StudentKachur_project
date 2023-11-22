def caesar_cipher(text, shift): #Функція ,яка шифрує текст шифром Цезаря з заданим зсувом
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char  # Додаємо неалфавітні символи без змін
            continue

        is_upper = char.isupper()
        char = char.upper()
        code = ord(char) + shift

        if code > ord('Z'):
            code = (code - ord('A')) % 26 + ord('A')

        cipher += chr(code) if is_upper else chr(code).lower()

    return cipher

text = input("Enter your message: ") #Користувач вводить текст дял шифрування

while True: #Нескінченний цикл , який запитує користувача значення зсуву по алфавіту
    try:
        shift = int(input("Enter the shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift value must be between 1 and 25 inclusive.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Тестування шифрування
result = caesar_cipher(text, shift)
print("Encrypted text:", result)
