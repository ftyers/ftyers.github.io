#### Which Unix command might you use to sort the output in frequency order?
```sort -nr
```

#### What do you think we would get if we set the argument reverse to False?
<br /> the list from the least frequent words to the most frequent
<br />

<br /> 1. My frequency list is in the file "reversecount" made by "count.py" which takes data from SynTagRus and outputs the list of words from the most frequent 
to the least frequent and their frequency correspondingly.<br />

<br /> 2. The file with the ranks of the mentioned words is called "ranks" <br />

<br /> 3. "Transliteration_table" file contains my rule for transliteration which are applied to the same SynTagRu file, the results are in 'translited'.
<br />

### Questions
#### What to do with ambiguous letters? For example, Cyrillic 'е' could be either je or e.
<br />
The resolving of this case is in "transliterate.py", I just track the context of this letter.
<br />

#### Can you think of a way that you could provide mappings from many characters to one character ?
	For example sh → ш or дж → c ? 
I would suggest making a command that checks wheather these letters come up together and if so - map them to one letter in the other language.

#### How might you make different mapping rules for characters at the beginning or end of the string?
Making the rule for each ambiguous letter: checking if it's at the beggining or at the end of the string and map to the corresponding spelling.
