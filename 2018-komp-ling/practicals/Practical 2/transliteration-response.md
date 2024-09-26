# Report on Transliteration  Task

We run into a couple of questions when going through the text of the tutorial, so firstly I would like to address them.
 
> Which Unix command might you use to sort the output in frequency order ?

We would sort it in Unix like this: `sort -k1 -n -r`

> What do you think we would get if we set the argument reverse to False ?

We would get an inverted frequency list, so the most frequent words would be in the end. Like this: [(21083, 'и'), (22727, 'в'), (45598, '.'), (70049, ',')]

## Ranking algorithm
Example of output:
```
1	21	,
2	8	.
3	7	и
4	6	в
5	4	не
6	4	его
7	4	был
8	3	с
9	3	он
10	3	Левы
```

I noticed an inverted dependency between rank and frequency: words with smaller rank have greater frequency.

> [(1, 21, ','), (2, 8, '.'), (3, 7, 'и'), (4, 6, 'в'), (5, 4, 'не'), ...]

As for the code, I think we can optimize it by just numerating our entries in the **sorted** frequency list (created by the code in freq.py) like this:

```
ranks = []
for counter in range(0, len(freq)):
    ranks.append((counter + 1, freq[counter][0], freq[counter][1]))
print(ranks)
```

## Transliteration
Code is transliterate.py, transliteration table is transl_dict.txt
Example output:
```
1	В	_	_	_	_	_	Translit=V
2	жизни	_	_	_	_	_	Translit=zhizni
3	Левы	_	_	_	_	_	Translit=Lyevy
4	Одоевцева	_	_	_	_	_	Translit=Odoyevtsyeva
5	,	_	_	_	_	_	Translit=,
6	из	_	_	_	_	_	Translit=iz
7	тех	_	_	_	_	_	Translit=tyekh
8	самых	_	_	_	_	_	Translit=samykh
9	Одоевцевых	_	_	_	_	_	Translit=Odoyevtsyevykh
10	,	_	_	_	_	_	Translit=,
11	не	_	_	_	_	_	Translit=nye
12	случалось	_	_	_	_	_	Translit=sluchalos'
13	особых	_	_	_	_	_	Translit=osobykh
14	потрясений	_	_	_	_	_	Translit=potryasyeniy
```
> What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.

I guess there the phonetic representation of a letter could help. As for the Russian language, the problem arises with consonants like 'е', 'ю', 'я', 'ё', which have different representations in different positions in a word. So we could write rules for every case. For instance:

```
vowels = ['а', 'о', 'у', 'и', 'э', 'ы']
signs = ['ъ', 'ь']
for num, letter in enumerate(line):
    if (num == 0 and letter == 'я') or\
                (letter == 'я' and num != 0 and (line[num-1] in vowels or\
                                                line[num-1] in signs):
        line.replace('я', ja)           # яблоко -> jabloko, статья -> stat'ja
    else:
        line.replace('я', '\'a')          # вязать -> v'azat'
```
(So there I guess I gave also an answer to the last question about different mapping rules)

Another issue concerning ambiguous letters is that some consonants also have different representations. For example: 'ц' can be 'ts' or 'c'.
In this case, I think it makes no important difference, so we can choose either variant for our "database". We are sure that nothing changes:
> красавица ____ Translit = 'krasavitsa'
> красавица ____ Translit = 'krasavica'


>  Can you think of a way that you could provide mappings from many characters to one character ?

There I think our previously used maxmatch algorithm could help.