word = input()
sample = '<>[]{}()'
new_word = ''

for i in word:
    if i in sample:
        new_word += i

while '<>' in new_word or '[]' in new_word or '()' in new_word or '{}' in new_word:
    new_word = new_word.replace('<>', '')
    new_word = new_word.replace('{}', '')
    new_word = new_word.replace('[]', '')
    new_word = new_word.replace('()', '')
if new_word:
    print(False)
else:
    print(True)
