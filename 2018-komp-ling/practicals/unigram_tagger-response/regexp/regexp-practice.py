import re

def delete_stress(text):
    return text.replace(chr(769), '')

def shashlyk():
    with open('Лингвистика.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = delete_stress(text)
        text = re.sub('Язык([аеиоувмх]{1,3}?)?([^а-я])', r'Шашлык\1\2',text)
        text = re.sub('([^а-я])язык([аеиоувмх]{1,3}?)?([^а-я])', r'\1шашлык\2\3', text)
    return text

def astronomy():
    with open('Философия.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = delete_stress(text)
        text = re.sub('Философи([еиюяйм]{1,3}[^а-я])', r'Астрологи\1', text)
        text = re.sub('([^а-я])философи([еиюяйм]{1,3}[^а-я])', r'\1астрологи\2', text)
    return text


def malaysia():
    with open('Финляндия.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        text = delete_stress(text)
        text = re.sub('Финлянди([еиюяй]{1,3}[^а-я])', r'Малайзи\1', text)
    return text


def main():
    with open('Лингвистика с шашлыком.txt', 'w', encoding='UTF-8') as f:
        f.write(shashlyk())
    with open('Астрология.txt', 'w', encoding='UTF-8') as f:
        f.write(astronomy())
    with open('Малайзия.txt', 'w', encoding='UTF-8') as f:
        f.write(malaysia())
    return 0


if __name__ == '__main__':
    main()

