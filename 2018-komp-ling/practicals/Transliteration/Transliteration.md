**Transliteration.**

*You'll note that the code does not print out the frequency list in order. Which Unix command might you use to sort the output in frequency order ?*  

Во-первых, мы используем команду sort. Наша сортировка должна быть числовой (мы сортируем по количественному значению встречаемости слова в тексте), т.е. добавляем флаг -n. В этом случае данные разместятся в арифметическом порядке (от меньшего к большему), а нам интересен обратный (от самых часто встречающихся слов к самым редким) —  флаг -r позволит получить желаемый результат. Получаем:
 
    sort -nr freq.txt > freq_sorted.txt


*What do you think we would get if we set the argument reverse to False ?*  

Применяя обратную сортировку к корпусу SynTagRus, мы получили в первую очередь самые часто встречающиеся токены — знаки препинания и предлоги (общие стоп-слова, которые чаще всего игнорируются, — при желании их можно исключить и из нашего сортированного списка, чтобы легче было добраться до более семантически нагруженных слов). Если в методе .sort() изменить аргумент на reverse=False, то в самом начале списка мы получим самые редкие токены — предполагаю, что это числа, значения температуры, редкие аббревиатуры и т.п., т.е. шумовые слова (как и в первом случае).    

*Ranking.*

Я решила еще раз потренироваться в сегментации - на этот раз в токенизации, поэтому решила взять текст повести Акутагавы Рюноскэ, разбить на токены, используя NLTK, нормализовать, сделать частотный список (freq_dictionary.py) и в конце концов провести ранжирование (rank.py - код оформлен таким образом, что аргумент берётся из командной строки, происходит чтение частотного списка из файла, этот список сортируется, а затем ранжируется; полученный список я направила в > monkey_ranked.txt). Больше всего в тексте повести оказалось запятых и точек, что неудивительно, - у них самые высокие ранги, 1 и 2. Сразу после них идут союзы и предлоги, то есть служебные части речи. В самом конце расположились уникальные слова, то есть встретившиеся один раз - у них самый низкий ранг среди токенов повести, 27. Словам, встретившимся одинаковое количество раз, присваивается один и тот же ранг; таким образом, даже не зная конретного значения частоты употребления того или иного слова, мы можем судить о том, какие слова встречаются чаще всего, какие слова по частнотности находятся на одном уровне (и можем, допустим, искать слова с интересующим нас уровнем частотности по заданному рангу). 

*Transliteration.*

В качестве опорных данных я использовала таблицу транслитерации водительских удостоверений Приказа МВД N 782 (в ней не используются диакритические знаки). Я создала файл rus-lat.tsv, который использовала для создания словаря соответствий. Из файла ru_gsd-ud-test.conllu (который я клонировала из репозитория UD) я извлекла второй столбец с текстом (с помощью `$ cut -f2 -d’ ‘`), предварительно очистив файл от комментариев. Скрипт transliterate.py делает из файла rus-lat.tsv словарь, а затем с его помощью переводит текст на русском в латинские символы и записывает полученный результат в файл trans_text.py. Я также транслитерировала уже упомянутую повесть Акутагавы Рюноскэ (monkey_transliterated.txt), успешно протестировав таким образом действие правила, согласно которому *Е/е* транслитерируется как *Ye/ye*, если стоит после гласных, *ъ*, *ь*.

*Questions.*  

1. Для неоднозначных букв (таких, например, как ‘e’, которая при транслитерации может превращаться в ‘e’ или ‘ye’) нужно придумывать дополнительные правила, выявляющие контекст для реализации того или иного типа соответствия: например, та же буква ’е’ изменяется на ‘ye’, если стоит в начале слова, идет после гласной или букв ‘ъ’ или ‘ь’, во всех остальных случаях её заменяет латинская ’e’. Эти правила я учла в коде transliterate.py  
2. Если стоит задача перевести многобуквенное выражение в однобуквенное (например, если нужно транслитерированный текст перевести в исходный), то нужно в первую очередь искать в строке именно эти многобуквенные выражения (используя правила или регулярные выражения), а потом уже остальные:  
    tsvetochnitsa → **ts**-veto-**ch**-ni-**ts**-a → цветочница  
Если подобный переход осуществляется не всегда (т.е. в каких-то случаях соответствие побуквенное), то нужно позаботиться о постулировании исключений.  
3. В наших правилах мы можем указать индекс символа, который нас интересует: если символ в начале строки — if line.index(char) == 0, если в конце — if line.index(char) == len(line). Еще вариант — использовать метод startswith() для проверки такого условия, как нахождение символа в начале строки, и метод endswith() — для активации правил, рассчитанных на символы в конце строки. 