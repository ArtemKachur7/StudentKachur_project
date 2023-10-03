user_word = input("Write your word: ")# Prompt the user to enter a word
user_word=user_word.upper()# and assign it to the user_word variable.
user_word_finally = ""
for letter in user_word:# for letter in user_word:
    if letter in "AEIOU": # Complete the body of the for loop.
        continue
        user_word_finally = letter
        print(letter)
    elif letter not in "AEIOU" :
        print(letter)
    else:
        break


