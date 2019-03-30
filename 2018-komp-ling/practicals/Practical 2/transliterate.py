
def read_text(filename):
    f = open(filename,'r', encoding='UTF-8')
    text = f.read()
    text = text.replace('\ufeff', '')

    return text


def write_new_text(filepath, text):
    new_text = open(filepath, 'w+', encoding='UTF-8')
    new_text.write(text)
    new_text.close()
    return new_text


def create_map(alphabets):
    lines = alphabets.split('\n')
    list_of_letters = []
    list_of_matches = []
    for line in lines:
        low_case = line.lower()     # because all letters in our table are in upper case
        list_of_letters.append(low_case)
        list_of_letters.append(line)
    for line in list_of_letters:
        letters = line.split('\t')
        list_of_matches.append(letters)
    matches = dict(list_of_matches)

    return matches


def transliterate(text, matches):
    transliterated_text = ''
    for letter in text:
        if letter in matches:
            if matches[letter] == '-':  # for Ъ and Ь
                transliterated_text += ''
            else:
                transliterated_text += matches[letter]
        else:
            transliterated_text += letter

    return transliterated_text


def main():
    alphabets = read_text('Transliteration_table.txt')
    matches = create_map(alphabets)
    text_to_transliterate = read_text('Text_to_transliterate.txt')
    transliterated_text = transliterate(text_to_transliterate, matches)
    print(transliterated_text)

    return write_new_text('Transliterated_text.txt', transliterated_text)


if __name__ == '__main__':
    main()
