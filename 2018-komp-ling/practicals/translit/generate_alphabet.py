'''rus_letters = []
print (ord('ё'), ord('Ё'))
print (ord('е'), ord('Е'))

print (1077 - 1105, 1045 - 1025)

for i in range (1040, 1104):
    if chr(i) == 'е':
        rus_letters.append(chr(i))
        rus_letters.append('ё')
    if chr(i) == 'Е':
        rus_letters.append(chr(i))
        rus_letters.append('Ё')
    else:
        rus_letters.append(chr(i))

print (rus_letters)'''

# Here is the russian alphabet:

rus_letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
eng_letters = ['A', 'B', 'V', 'G', 'D', 'E', 'Yo', 'Zh', 'Z', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'Kh', 'Ts', 'Ch', 'Sh', 'Shch', "'", 'Y', "'", 'E', 'Yu', 'Ya', 'a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', "'", 'y', "'", 'e', 'yu', 'ya']

'''for i in range(len(eng_letters)):
    eng_letters.append(eng_letters[i].lower())'''

print (eng_letters)

with open('trans_dict.txt', 'w') as f:
    for i in range(len(rus_letters)):
        f.write('{}\t{}\n'.format(rus_letters[i], eng_letters[i]))
