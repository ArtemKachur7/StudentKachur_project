def is_prime(num): #Функція перевірки чи є задане число простим
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#тестуючий код
for i in range(2, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()