
## Tokenization

Поледовательность задач:
1. Создадим список уникальных словоформ (wordlist) из тренировочного набора UD_Japanese-GSD.
2. Получим из тестового набора UD_Japanese-GSD список исходных предложений для токенизации (sentences).
3. Получим из тестового набора UD_Japanese-GSD список предложений, уже разбитых на токены (reference_sentences).
4. Используем max_match для токенизации тестового набора исходных предложений (sentences).
5. Посчитаем качество токенизации (WER). Вычислим расстояние Левенштейна для списка токенов исходного предложения (reference_sentence) и списка токенов, полученных при токенизации предложения алгоритмом maxmatch (hypothesis_sentence).


```python
# функция, которая создает список уникальных словоформ (wordlist) для использвоания в max_match
def wordlist_extract(filename):
    with open(filename, "r", encoding="utf-8") as f:
        l = f.readlines()
        wordlist = []
        for line in l:
            if line[0].isdigit():
                s = line.split("\t")
                wordlist.append(s[1])
        wordlist = set(wordlist)
        return list(wordlist)
```


```python
# 1. Создадим список уникальных словоформ из тренировочного набора UD_Japanese-GSD
wordlist = wordlist_extract('ja_gsd-ud-train.conllu')
```


```python
# всего получилось 22 313 словоформ
len(wordlist)
```




    22313




```python
# посмотрим первые десть
wordlist[0:10]
```




    ['藩', 'フース', '認める', '往々', '中間報告', 'ビール', '馬小屋', 'アイディア', '懐疑的', '敷き詰める']




```python
# 2-3. Вытащим предложения для токенизации и токены для референса из тестового набора UD_Japanese-GSD
sentences = []
reference_sentences = []
print_count = 0
with open('ja_gsd-ud-test.conllu', "r", encoding = 'utf-8') as data:
    parsed_sentence = [] 
    for line in data:
        row = line.split('\t')
        if('# text =' in row[0]):
            sentences.append(row[0][8:-1])
        if(str(row[0]).isdigit()):
            parsed_sentence.append(row[1])
        else:
            if parsed_sentence:
                reference_sentences.append(parsed_sentence)
            parsed_sentence = []
```


```python
# Посмотрим на два исходных предложения
sentences[0:2]
```




    [' これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。',
     ' 幸福の科学側からは,特にどうしてほしいという要望はいただいていません。']




```python
# Посмотрим на токены, которые получились из исходных предложений
reference_sentences[0:2]
```




    [['これ',
      'に',
      '不快感',
      'を',
      '示す',
      '住民',
      'は',
      'い',
      'まし',
      'た',
      'が',
      ',',
      '現在',
      ',',
      '表立っ',
      'て',
      '反対',
      'や',
      '抗議',
      'の',
      '声',
      'を',
      '挙げ',
      'て',
      'いる',
      '住民',
      'は',
      'い',
      'ない',
      'よう',
      'です',
      '。'],
     ['幸福',
      'の',
      '科学',
      '側',
      'から',
      'は',
      ',',
      '特に',
      'どうして',
      'ほしい',
      'という',
      '要望',
      'は',
      'いただい',
      'て',
      'い',
      'ませ',
      'ん',
      '。']]




```python
# max_match
# sentence – предложение, которое предстоит токенизировать
# wordlist - список уникальных словоформ, по которым происходит поиск токенов
def max_match(sentence, wordlist):
    if not sentence:
        return []
    for i in range(len(sentence)-1, -1, -1):
        first_word = (sentence[0:i+1])
        remainder = sentence[i+1:len(sentence)]
        if first_word in wordlist:
            return [first_word] + max_match(remainder, wordlist)

    # если слово не найдено, то создаем новое односимвольное слово
    first_word = sentence[0]
    remainder = sentence[1:len(sentence)]

    return [first_word] + max_match(remainder, wordlist)
```


```python
# 4. Токинизируем max_match'ем первые 100 предложений
hypothesis_sentences = []
for sentence in sentences[0:99]:
    hypothesis_sentence = max_match(sentence.strip(), wordlist)
    hypothesis_sentences.append(hypothesis_sentence)
```


```python
# Посмотрим на два первых предложения, токенизированных max_match'ем
hypothesis_sentences[0:2]
```




    [['これ',
      'に',
      '不快',
      '感',
      'を',
      '示す',
      '住民',
      'は',
      'いま',
      'し',
      'たが',
      ',',
      '現在',
      ',',
      '表',
      '立っ',
      'て',
      '反対',
      'や',
      '抗議',
      'の',
      '声',
      'を',
      '挙げて',
      'いる',
      '住民',
      'は',
      'い',
      'ない',
      'ようで',
      'す',
      '。'],
     ['幸福',
      'の',
      '科学',
      '側',
      'から',
      'は',
      ',',
      '特に',
      'どうして',
      'ほしい',
      'という',
      '要望',
      'は',
      'いただい',
      'て',
      'いま',
      'せ',
      'ん',
      '。']]




```python
# функция для расчета качества токенизации (WER)
# https://martin-thoma.com/word-error-rate-calculation/
import sys
import numpy


def editDistance(r, h):
    '''
    This function is to calculate the edit distance of reference sentence and the hypothesis sentence.
    Main algorithm used is dynamic programming.
    Attributes: 
        r -> the list of words produced by splitting reference sentence.
        h -> the list of words produced by splitting hypothesis sentence.
    '''
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0: 
                d[0][j] = j
            elif j == 0: 
                d[i][0] = i
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitute = d[i-1][j-1] + 1
                insert = d[i][j-1] + 1
                delete = d[i-1][j] + 1
                d[i][j] = min(substitute, insert, delete)
    return d


def getStepList(r, h, d):
    '''
    This function is to get the list of steps in the process of dynamic programming.
    Attributes: 
        r -> the list of words produced by splitting reference sentence.
        h -> the list of words produced by splitting hypothesis sentence.
        d -> the matrix built when calulating the editting distance of h and r.
    '''
    x = len(r)
    y = len(h)
    list = []
    while True:
        if x == 0 and y == 0: 
            break
        elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1] and r[x-1] == h[y-1]: 
            list.append("e")
            x = x - 1
            y = y - 1
        elif y >= 1 and d[x][y] == d[x][y-1]+1:
            list.append("i")
            x = x
            y = y - 1
        elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1]+1:
            list.append("s")
            x = x - 1
            y = y - 1
        else:
            list.append("d")
            x = x - 1
            y = y
    return list[::-1]


def wer(r, h):
    """
    This is a function that calculate the word error rate in ASR.
    You can use it like this: wer("what is it".split(), "what is".split()) 
    """
    # build the matrix
    d = editDistance(r, h)

    # find out the manipulation steps
    list = getStepList(r, h, d)

    # print the result in aligned way
    result = float(d[len(r)][len(h)]) / len(r) * 100
    #result = str("%.2f" % result) + "%"
    return result
```


```python
# 5. Посчиатем ошибку для первого пердложения
wer(reference_sentences[0], hypothesis_sentences[0])
```




    37.5




```python
# Посчиатем ошибку для первых ста пердложений
wer_for_sentences = []
for i in range(99):
    wer_for_sentence = wer(reference_sentences[i], hypothesis_sentences[i])
    wer_for_sentences.append(wer_for_sentence)
```


```python
# Медианное значение ошибки, рассчитанной для первых ста предложений
print(numpy.mean(wer_for_sentences))
```

    21.858267979839734



```python

```
