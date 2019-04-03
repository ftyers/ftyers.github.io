## Install udpipe  

Я начала было обучать модель, но после n-ной эпохи мне не хватило терпения -- и я скачала предобученную модель. Взяла отрывок из повести Чехова "Черный монах" и запустила, как было написано в практикале:  
`$ cat black_monk.txt | udpipe --tokenize --tag --parse > black_monk.conllu`
Однако bash любезно подсказал, что синтаксис немного другой:  
`udpipe [running_opts] model_file [input_files]`
Исправляю -- и всё получается:  
`$ cat black_monk.txt | udpipe --tokenize --tag --parse ru_syntagrus-ud.udpipe > black_monk.conllu`
Уже знакомый Udpipe проанализировал все токены.  

## Xrenner

Как и было рекомендовано, в субдиректории xrenner/models я создала директорию с трёхбуквенным кодом языка: xrenner/models/rus, все настройки скопировала из базовой модели /udx.  
Дальше я запустила xrenner на полученном на предыдущем шаге файле conllu:  
`$ python3 xrenner.py -m rus html black_monk.conllu > /tmp/black_monk.html`
И получила красиво подсвеченный html, в котором были успешно разрешены некоторые кореференции, например:   

-- [Меня]  сегодня с самого утра  занимает [[одна легенда]]. -- Не помню, вычитал ли [я] [[её]] <...>.  
  
А дальше все было уже не так весело.  
Я попыталась внести правки/дополнения в некоторые важные файлы, которые были упомянуты (и которые необходимы, чтобы приспособиться к определённому языку):  

`coref_rules.tab`

В документации я посмотрела, по какому принципу строятся правила:  
`ANA;ANT;DIST;PROP(;CLF(;THRESH))`

Изучила первое правило:  
`#first match identical proper markables
form="proper";form="proper"&text=$1&take_first;100;nopropagate`

-- The first rule below illustrates a very ‘safe’ strategy, searching for proper noun markables with identical text (=$1) in the previous 100 sentences, since these are almost always coreferent, and undertaking no feature propagation.    

И попыталась создать своё правило, которое бы было релеватным для моего отрывка:  

`form="common";form="common"&lemma=$1&take_first;2;nopropagate`

то есть должны соотноситься в пределах этого и 2-х предыдущих предложений слова form='common', у которых леммы идентичны. Ожидаем, что разрешится кореференция 'мираж' - 'миража', но этого не происходит.       

Потом пробуем справиться с кореференцией в пределах одного предложения '<...> рыбаки  видели [другого черного монаха], [который] <...>':         

`text=/^который$/;func=/obj/&take_first;0;propagate`

Тоже без изменений.           

От отчаяния пробуем соотносить все одинаковые леммы:    

`lemma=/.*/;lemma=$1;100;nopropagate`

Ничего.    

`pronouns.tab`

Одновременно с вышеперечисленным были внесены такие изменения:   

    который	male
    которая	female
    который	2sg
    которая	2sg
    он	male
    онa	female
    ее	female
    его	male
    которых	3pl

Улучшений не произошло.   

`entities.tab`

Здесь попробовала добавить вот что (в отрывке не так много сущностей, которые выжны для разрешения кореференции):     

    монах	person	person/male	1

Видимо, я делаю что-то принципиально не то -- надеюсь, у меня еще будет возможность разобраться с Xrenner, понять его.   




