word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Insert here a word: ")
user_word = user_word.upper()
number_of_letters = len(user_word)

count = 0


for count in range(number_of_letters):
    if user_word[count] == "A":
        continue
    elif user_word[count] == "E":
        continue
    elif user_word[count] == "I":
        continue
    elif user_word[count] == "O":
        continue
    elif user_word[count] == "U":
        continue
    word_without_vowels = word_without_vowels + user_word[count]
    count = count + 1

print(word_without_vowels)
