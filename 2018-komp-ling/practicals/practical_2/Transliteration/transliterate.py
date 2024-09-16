import sys


def opn(file):
    letters = {}
    with open(file) as f:
        for line in f.read().splitlines():
            row = line.split('\t')
            cyr = row[0]
            letters[cyr] = row[1]
    return letters

# словарь, корректно работающий с этим кодом, не должен содержать букв 'е' и 'ё'

def translit(text, dict):
    vowels = ['а', 'e', 'и', 'о', 'ё', 'у', 'ы', 'э', 'я', 'ю']
    n = 0
    final = ''
    for w in text:
        if w == 'е':
            if n == 0:  # проверка на первую букву текста, чтобы не убежало на [-1]
                final += 'je'
            elif text[n-1] not in vowels:
                final += 'е'
            else:
                final += 'je'
        if w == 'ё':
            if n == 0:
                final += 'jo'
            elif text[n-1] is 'ж' or 'ш' or 'ч' or 'щ':
                final += 'o'
            else:
                final += 'jo'
        if w == ' ':
            final += ' '
        if w in dict:
            final += dict[w]
        n += 1

    print(final)
    return final


def main():
    return translit(' '.join(sys.argv[1:]), opn('trans.txt'))

if __name__ == '__main__':
    main()

