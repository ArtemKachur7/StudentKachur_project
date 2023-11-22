def mysplit(string, space=None): # Написати метод аналогічний split()
    result = []
    start = 0
    if space is None: # Перевірка наявності пробіла або роздільника, якщо немає додаємо пробіл
        space = ' '

    while start < len(string): # Виокремлюємо рядок
        end = string.find(space, start)
        if end == -1:
            end = len(string)

        result.append(string[start:end]) # Записуємо рядок
        start = end + len(space)

        while start < len(string) and string[start:start + len(space)] == space: # Пропускаємо додаткові роздільники
            start += len(space)
    return result

#Тестуємо функцію
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit("abc"))
print(mysplit(""))
