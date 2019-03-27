# Practical 2
Here's to some questios from practical 2:
>You'll note that the code does not print out the frequency list in order. Which Unix command might you use to sort the output in frequency order ?

```sort -nr```

>What do you think we would get if we set the argument reverse to False ?

We'd get an ascending sorted list.

Firstly, I made [rank.py](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%202/rank.py) which takes a command line argument and reads in a frequency list from a file and outputs a ranked frequency.
Then I [implemented transliteration algo](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%202/transliterate.py), discribed in the task. 

>What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.

Russian _e_ could be either je after _ь_, _ъ_, vowels and at the beginning of the word or _e_ in all the other cases. So, we can add some rules to disambiguate it. We can apply it either before or after transliteration. For example, after transliteration we can look at every _e_ in transliterated text and replace it with _je_ if it stays after [AOIEUaoieu']. 

>Can you think of a way that you could provide mappings from many characters to one character ?
>For example sh → ш or дж → c ?

Maybe we can firstly go through all the text to find _sh_ and replace it with _ш_ or _дж_ with _j_ annd so on and then do it one more time to replace remaining letters.
>How might you make different mapping rules for characters at the beginning or end of the string ?

In the case of Russian-to-Englich transliteration we could have troubles at the beginning of the word only with _e_, I guess. We can write something like:
```
  if str.startswith(letter):
  ...
```
If we are afraid to lose upper cases at the beginng of the sentence, we could add them in our mathes table or just implement simple rule I described above.
