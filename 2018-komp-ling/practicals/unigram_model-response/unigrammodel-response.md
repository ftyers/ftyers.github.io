**Functions**<br>

$ python3 palindrome.py<br>

part of the output (freq.txt):<br>
```
3439    как  
1669    или  
1254    еще  
1085    ее  
283     тут  
279     тот  
190     оно  
90      XX  
80      11  
71      XIX  
71      2002  
64      ими  
31      СПС  
28      II  
28      1991  
27      22  
21      дед  
18      мм  
17      55  
16      доход  
```
**Implementing n dimensional matrices with dict**  
$ python3 matrix.py  
```
        a       absorbed        all     and     another  
бы      0       0       0       0       0  
вас     0       0       0       0       0  
видит   0       0       0       0       0  
всего   0       0       0       0       0  
вы      0       0       0       0       0  
```
- _Why do we need end='' passed to the print() statement ? What would happen if we didn't have it ?_  
- '\n' after each element  
```
  a       absorbed        all     and     another  
бы  
0  
0  
0  
0  
0  
```
**Passing arguments from the command line**  
$ python3 args.py a b c  
- _What output do you get ?_  
- List of the command line arguments passed to the script:  
['args.py', 'a', 'b', 'c']  

**Unigram language model**  
The code with comments is in "train.py", reasults are in "output.txt", the first column is a probability 
of each POS-tag =(number of appearence of this tag in corpora)/(number of all the tags) 
or the probability that given word appears with given tag in corpora (appearences of this word with this tag)/
all the appearences of this word), then there is a tag itself, then number of all appearenes of the word
and then the word itself. (Well I should've probably delete repeated words from output, but it doesn't affect the results anyway.)

- _What might be a simple improvement to the language model for languages with orthographic case ?_  
- Well I just used syntagrus data where each word have a normalized and lowered form. But it is easy 
to lowercase all the words yourself and make some exceptions for the words from proper nouns dictionary.
