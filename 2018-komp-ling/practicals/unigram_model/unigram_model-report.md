# Practical 3 - Unigram model

 - Why do we need end='' passed to the print() statement ? What would happen if we didn't have it ?
 End='' makes the next print() to be printed right after the previous print, without going to the next line (it is default end). If we don't have end='', the numbers in matrix will go one below another (in a column), for example:
```
бы	
0	
0	
0	
0	
0
```

- After the command
```
python3 args.py a b c
```
I get the following output:
```
['args.py', 'a', 'b', 'c']
```

## Instruction to train.py file
 - Run train.py in the terminal as follows:
```sh
python3 train.py corpora.txt > results.txt
```
where corpora.txt - .conllu-like file with sentences and its analysis (downloaded from UD github), results.txt - the output file.

__For languages with orthographic case__ a simple improvement would be done by changing one line (word = ...) in the train.py:
```python
word = element[1]
pos = element[3]
# we check whether the word is in dictionary: if not we create an empty dict for that
if word not in word_tag:
    word_tag[word] = Counter()
# we fill the dict of the word with its POS and count the number of that word+POS
word_tag[word][pos] += 1
# we add POS tag and count it
tag_count[pos] += 1
# we count total amount of words we have
total_count += 1
```