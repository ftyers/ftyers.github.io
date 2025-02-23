def trans(text):
    text = text.split()
    alphabet = [chr(i) for i in range(97,123)]
    for word in text:
        if word[-1:] in alphabet:
            if word[-2:] in ['ch','sh','tz'] or word[-1:] in ['s','x']:
                new_word = word + 'es'
                print(new_word)
            else:
                new_word = word + 's'
                print(new_word)
        else:
            if word[-3:-2] in ['ch','sh','tz'] or word[-2:-1] in ['s','x']:
                new_word = word + 'es'
                print(new_word)
            else:
                new_word = word + 's'
                print(new_word)
    text = ' '.join(text)
    return text


def main():
    text = input('Please enter the line of nouns:')
    return trans(text)


if __name__ == '__main__':
    main()