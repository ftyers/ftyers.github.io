# Report 3
## Transliteration
### Sorokin Semen

I have tried to lead HFST guide, but it was to difficult to finilisy it. 
Therefore I implement transliteration script with Python. The script contains four functions with *main*. 

First one clears UD-corpus-like objects to prepare test data, the second one opens txt-file containing pairs of symbols to replace with. The third one produces a transliteration and in the "main" I apply it to the date from stdin and implement strdout using "print" function. 

Q&A: 
Replacing two characters with one letter is implemented using dict and tuples in Python.
Initial and finishing characters were detected using string indexes.

To use it you can write a command like this: *"python3 Translit.py ud_russian.txt symbol_dict.txt"* where *Translit.py* is a script, *ud_russian.txt* - test sentences to transliterate and *symbol_dict.txt* is a symbols-pair dictionary. In the file *result.txt* you can see cleared Ud sentences and result of transliteration in the last column.
