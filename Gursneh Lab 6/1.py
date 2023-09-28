sen = (input("enter a sentence :"))
count_vowel = 0
count_consonants = 0
count_words = 1
vowels = ['a','e','i','o','u','A','E','I','O','U']

for i in (sen):
    if i in vowels:
        count_vowel += 1
    elif i == ' ':
        count_words += 1
    else:
        count_consonants += 1
print(count_vowel)
print(count_consonants)
print(count_words)
