# Report on Transliteration  Task

We run into a couple of questions when going through the text of the tutorial, so firstly I would like to address them.
 
> Which Unix command might you use to sort the output in frequency order ?

We would sort it in Unix like this: `sort -k1 -n -r`

> What do you think we would get if we set the argument reverse to False ?

We would get an inverted frequency list, so the most frequent words would be in the end. Like this: [(21083, 'и'), (22727, 'в'), (45598, '.'), (70049, ',')]

## Ranking algorithm
I implemented the ranking algorithm described in the tutorial and, firstly, I found out that the most frequented word somehow was out of the list, so I added a string in order not to lose it:

```
rank = 1
minim = freq[0][0]
ranks = []
ranks.append((rank, freq[0][0], freq[0][1])) # This one
for i in range(1, len(freq)):
...
```

Secondly, I noticed an inverted dependency between rank and frequency: words with smaller rank have greater frequency.

> [(1, 3727, 'год'), (2, 2015, 'время'), (3, 1258, 'день'), (4, 1200, 'рука'), ...]

As for the code, I think we can optimize it by just numerating our entries in the sorted frequency list like this:

```
ranks = []
    for counter in range(0, len(freq)):
        ranks.append((counter + 1, freq[counter][0], freq[counter][1]))
    return ranks
```

## Transliteration

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