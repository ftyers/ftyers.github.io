### udpipe
Я взяла готовую модель и  файл ```paragraph.txt```. В результате получла файл ```paragraph.conllu```
```bash
$ cat paragraph.txt | udpipe --tokenize --tag --parse ru_syntagrus-ud.udpipe > paragraph.conllu
```
Аннотация прошла не без ошибок, например, токен "пищало" был определён как существительное, хотя в данном тексте является глаголом.
### xrenner
Я создала директорию /rus и скопировала базовые настройки модели /udx, внеся изменения в соответствии с аннотируемым текстом:
```pronouns.tab```
```
он	male
его	male
ему	male
```
```entities.tab```
```
достоевский	person	person/male	1
ф.	person	person/male	1
м.	person	person/male	1
федор	person	person/male	1
кот	animal	animal	1
роман	object	object	1
животное	animal	animal	1
```
```conf.ini```
```
proper_pos=/PROPN/
```
Эксперименты с ```entity-heads.tab```, ```coref.tab```, ```names.tab``` не привели к улучшению разрешения кореференции. Также я пробовала изменить первое правило *(The first rule below illustrates a very ‘safe’ strategy, searching for proper noun markables with identical text (=$1) in the previous 100 sentences, since these are almost always coreferent, and undertaking no feature propagation.)* так, чтобы оно работало для русского языка (Достоевский-Достоевского), и прописала идентичность не текста, а леммы, но это не помогло.
``` coref_rules.tab```
```
#first match identical proper markables
form="proper";form="proper"&lemma=$1&takefirst;100;nopropagate
```
Результат - в файле ```paragraph.html```
```bash
$ python3 xrenner.py -m rus -o html paragraph.conllu > /tmp/paragraph.html
```
