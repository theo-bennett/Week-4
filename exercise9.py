# Lab 4 - Exercise 9: Anagrams

first_word = input("Enter the first word: ").upper()
second_word = input("Enter the second word: ").upper()

# Same letters with the same frequency -> sorted letters are identical
print(sorted(first_word) == sorted(second_word))
