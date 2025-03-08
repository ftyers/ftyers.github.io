# Report on unigram model by Nikolaeva Anna

### 1. Implementing n-dimensional matrices with dict

We need the end="" parameter in order to print values of the inner dictionary on the same line, where we print the dictionary key. 
If we don't use end="", Python would think, that we want to print every element of the dictionary on a new line (end="\n" by default, when we use the "print" function). Without this parameter we will not get the matrix, but we'll get the structure like:
```
бы
0
0
0
0
0
0

вас
0
0
0
0
0
0
```
### 2. Passing arguments from the command line
The question: how do you get from that command line to having the filename as a variable you can use in your program? 
If I understand the question right, in order to have the filename as a variable, we need to pass the name of our file to the command line after the program name and use "<", for example:
```
$ python3 train.py < rus-eng.tsv 
```
It means that the program train.py takes the file rus-eng.tsv as a variable. To use the "rus-eng.tsv" file as a variable, we need to have a sys module imported in our code and write in the code something like:
```
f = sys.sdtin.readlines()
```

The command 
```
$ python3 args.py a b c 
```
returns a list of arguments ['args.py', 'a', 'b', 'c']. The first argument is the name of the file with our code, the rest elements in the list are additional arguments, which we passed to our program in the command line.   

### 3. Unigram language model
You can see my Python code in train.py. It takes any file in a ".conllu" extension as input in a command line and outputs a matrix of POS-tags and words probability and frequency into standart output. I was using the SynTagRus corpus part as input (13 annotated sentences in "1.conllu") to create the matrix, my output can be seen in a file named "unigram.tsv". 

If we want to make our model case-insensitive, we may convert every word in our data to lowercase, using a method string.lower(). My code would change a little bit (see modifications and comments in train_case.py).

After changing the case, the output would change as well. If you compare my output files "unigram.tsv" and "unigram_case.tsv", in the second one the frequencies of adpositions "В" and "в" have summed up. In my case only frequency column (a "count" column) of the token changes, and we get a less number of lines in the output. But if the same word has different POS-tags in upper and lower cases, we may get different results in the probability column too. 

On the other hand, it may not be good for the language model to get proper nouns in lowercase too. To avoid this, we may create and/or use a certain dictionary of proper nouns and check, if a word from our corpus is in this dictionary, before converting the word to lowercase. If the word is in the proper nouns dictionary, we will not apply the string.lower() method to this word.  







