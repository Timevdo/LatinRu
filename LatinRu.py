import re

russianWords = open('russianWords50000.txt','r', encoding='utf8')
russianWords = russianWords.readlines()

badLetters = re.compile('[бгджзийлпфцчшщьъыэюя]')

longestWord = ""
i = 0

for word in russianWords:
    percent = str((i/50000)*100)[0:2] + "%"
    print(percent, end='\r')

    if len(word) < len(longestWord):
        i += 1
        continue
    
    if re.search(badLetters, word):
        i += 1
        continue
    
    longestWord = word
    i += 1

print(longestWord)