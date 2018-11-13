## Отчет по транслитерации

При составлении таблицы транслитерации с русского на английский я ориентировался на приказ МВД (2010) для транслитерации имён и фамилий в загранпаспортах.

[Таблица транслитерации](table.tsv)


Из таблицы я сделал словарь, а затем реализовал алгоритм транслитерации с учетом дополниетльных правил для разрешения неоднозначности с Е и Ё. Буква Е (Ё) русского алфавита транслитерируется в латинский алфавит как Ye, если стоит в начале слова, после гласных и знаков Ъ и Ь. Во всех остальных случаях – как E.

Чтобы учесть контекст для разрешения неоднозначности с Е и Ё, я отдельно сохраняю предыдущий символ. Таким образом последовательности вида 'ое', 'ие' и т.д. переходят в 'oye', 'iye' и т.д. Начало слово я определяю по наличию пробела перед буквой Е (Ё).

```
trans_text = []
current_char = ['start']
context_for_ye = [' ', 'а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'ъ', 'ь']

for letter in text:
    if letter in trans:
        previous_char = current_char.pop()
        if letter == 'е' or letter == 'ё':
            if previous_char in context_for_ye:
                char = 'ye'
            else:
                char = 'e'
        elif letter == 'Е' or letter == 'Ё':
            if previous_char == ' ':
                char = 'Ye'
            else:
                char = 'E'
        else:
            char = trans[letter]
        current_char.append(letter)
        trans_text.append(char)

output_text = ''.join(trans_text)
```

[Подробный код](transliterate.py)


**Пример работы алгоритма**

> Съешь ещё этих мягких французских булок, да выпей же чаю. Тёмное дерево ёлка. В Елец приехал огурец! АУЕ?

> S″yesh' yeshche etikh myagkikh frantsuzskikh bulok, da vypey zhe chayu. Temnoye derevo yelka. V Yelets priyekhal ogurets! AUE?


