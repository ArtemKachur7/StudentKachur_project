def add_phone_number(phone_book, contact_name, new_phone_number): #Функція , яка додає новий номер телефону для вказаного контакту в телефонну книгу.
    if contact_name in phone_book: # Якщо контакт існує, додати новий номер телефону до списку
        phone_book[contact_name].append(new_phone_number)
    else: # Якщо контакт не існує, створити новий запис у словнику
        phone_book[contact_name] = [new_phone_number]

def print_phone_numbers(phone_book):#Функція , яка виводить на екран список номерів телефонів для всіх контактів в телефонній книзі.
    print("Список номерів телефонів для контактів:")
    for contact_name, phone_numbers in phone_book.items():
        print(f"{contact_name}: {', '.join(phone_numbers)}")

phone_book = {} # Початкова пуста телефонна книга

while True:
    contact_name = input("Введіть ім'я контакту (або Enter, щоб завершити): ")
    if contact_name == "":
        break
    phone_number = input("Введіть номер телефону для додавання: ")

    add_phone_number(phone_book, contact_name, phone_number)# Додаємо новий номер телефону до контакту


print_phone_numbers(phone_book) # Виводимо список номерів телефонів для всіх контактів