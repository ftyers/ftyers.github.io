# Practical 2: Transliteration (engineering)

<div style="column-width: 30em">

## Questions
What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.

Can you think of a way that you could provide mappings from many characters to one character ?
        For example sh → ш or дж → c ?
How might you make different mapping rules for characters at the beginning or end of the string ?


### Правила для транслитерации

Основная идея - это начинать транслитерацию со сложных, многобуквенных преобразований (ч - tch). Например:
>Шарик -- sh-арик -- sharik

Далее нужно заменить все гласные в начале и в конце слова (Я - ya). 
>яблоко -- ya-блоко -- yabloko

После чего уже можно переходить на простые однобуквенные преобразования (у - u)
>мед -- med

## Методы
### Кодировка-декодировка с помощью KOI-8R

Транслитерация с помощью кодировки KOI-8R - не самый эффективный метод транслитерации текста. 
Но он обеспечивает некоторые особенности, которые не доступны другим способам:

    1)Возможность восстановить первоначальный текст

    2)Правила кодировки уже заданы

Метод транслитерации с помощью KOI-8R представлен в файле transliterate_koi8r.py

### Кодировка-декодировка с помощью правил

Правила для транслетерации находятся в файле rules.txt.
 В нем заданы правила для согланых, гласных, а также для гласных в начале слова.


</div>
