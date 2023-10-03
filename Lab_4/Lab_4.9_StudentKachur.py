word_without_vowels = ""
user_word = input("Write your word: ")# Prompt the user to enter a word
user_word=user_word.upper()# and assign it to the user_word variable.
for letter in user_word: # for letter in user_word:
    if letter in "AEIOU":  # Complete the body of the loop.
        continue
    word_without_vowels += letter
print(word_without_vowels)# Print the word assigned to word_without_vowels.

