# Transliteration

This Practical was not so difficult for me. In my report I will answer the questions during the Practical and comment on some points. 

## 1. After counting frequency of words in some text we may use the following Unix command to sort the output in frequency order:
```
sort -nr freq.txt > freq-sorted.txt 
```
## 2. After running the code with freq.sort() on SynTagRus test.conllu file, I got the following result: 
```
ann@ann-VirtualBox:/media/sf_share_ubuntu/UD_Russian-SynTagRus$ python3 vocab_freq.py < ru_syntagrus-ud-test.conllu
reverse=True:  [(9122, ','), (6015, '.'), (3135, 'в'), (2968, 'и')]
reverse=False:  [(1, '0,4'), (1, '00'), (1, '03'), (1, '1 200 000')]
```
We can see that the most frequent words are punctuation and so-called stop-words (prepositions and conjunctions). We get them using the method freq.sort(reverse=True, freq[0:4]).  On the other hand, if we use reverse=False parameter, we get the words with lowest frequency, starting from the smallest number. 

## 3. About ranking. 

As far as I understand, ranking can make the text analysis simplier. Ranking allows us, depending on the task, to choose the word of higher frequency more quickly or in a more effective way; if, for example, we need to choose between two or more synonyms. In this context knowing a rank of the word is enough, and we don't need to learn the exact frequency of the word. Maybe ranking is useful for some statistical research. (Although I am not confident in my correct understanding of the idea of ranking).

You may see my ranking of test.conllu file in ranks.txt. 
We can see, that the higher the rank, the less frequent is the word under this rank. Words with equal frequency get same ranks.

As I am not so good at Python yet, unfortunately, I do not know, how we can optimitize the code in _rank.py_, but would like to know about it.

# 4. I decided to make the transliteration of the written Komi-Zyrian language from the test.conllu file, that I cloned from https://github.com/UniversalDependencies/UD_Komi_Zyrian-Lattice. 

My program _transliterate.py_ makes a dictionary from the Komi-Zyrian alphabet and it's transliteration (see alpha-komi-zyrian.tsv). I copied the transliteration from the Wikipedia article about Komi-Zyrian. 

My program takes two arguments: the source file (kpv_lattice-ud-test.conllu) and the output file (transliterated.conllu), and stores the transliteration in the Miscellaneous column of the output file. I have chosen the 9th column for transliteration, as it seems empty for all words. 

# 5. The answers to the questions after the practical:

- What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.

The answer: I think we could write a context rule in our code (using the condition 'íf') that says in which positions - inside or between words - 'je' occurs or 'e' occurs. For example, if it is the beginning of the word or the previous letter is a vowel, we transliterate 'e' as 'je'. Also we could include this constraint in FST phonological rules. Or we can use ranking, if, for example, the difference of pronounciation depends on the the area where native speakers live.   
To conclude, I think there is a plenty of ways to write such rules, depending on our purpose. Maybe for some tasks such division of transliteration is not necessary. 

- Can you think of a way that you could provide mappings from many characters to one character ? For example sh → ш or дж → c ?

The answer. I thought on that a lot. My first idea is to use regular expressions to change the wrong transliteration to the correct one before writing it in a file, and I used this method in my code. 
The other possible way is as follows. In case of 'sh', when the program checks if 's' in the dictionary, it should also check, if the next symbol is 'h'. If yes, the program should search the key 'sh' in the dictionary. In my opinion, it's more elabotare, than writing regular expressions. I would like to know other ways to provide such mappings. 

- How might you make different mapping rules for characters at the beginning or end of the string ?

The answer. I cannot imagine the purpose of that, but apparantly we may create another dictionary for special cases and use the "if" condition and some methods, such as str.startswhith(...) or str.endswith(...): depending on trueness or falseness the program would choose the right dictionary to refer. 



