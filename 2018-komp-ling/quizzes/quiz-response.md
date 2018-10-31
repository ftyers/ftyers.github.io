# Quiz_01
##### Anastasiya Lisitsyna

1. Which problems does maxmatch suffer from? (Choose all that apply.)

**a) requires comprehensive dictionary**
b) is computationally expensive
c) is difficult to program
**d) constructs non-grammatical sentences**

2. Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2":

```sh
$ head test.txt
kot/obormot
1/2
$ sed 's/\([[:alpha:]]\+\)\/\([[:alpha:]]\+\)/\1 \/ \2/g' test.txt 
kot / obormot
1/2
```

3. The text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?
 - requires corpora of marked-up text
 - requires more computational cost
 - problems with interpretation - ML is like a blackbox

4. Write a sentence (in English or in Russian) which maxmatch segments incorrectly.
I confirm my attendance. -> Iconfirmmyattendance. -> Icon firm my attendance.

5. What are problems for sentence segmentation? provide one example in English or Russian for each that applies.

**a) ambiguous abbrevations with punctuation**
*Hermione Granger founded S.P.E.W. in 1994.*
**a) sentences containing symbols '!' and '?'**
*In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.*
**a) sentences lacking separating punctuation**
*I missed dot after this sentence It is the next sentence.*
**a) sentences not separated by whitespace**
If rule-based segmentation is based on the assumption that sentences are divided by construction "some punktuation sign + whitespace + word which starts from uppercased letter", it will cause problems for sentence segmentation.
*This is an example.I see no space.*
