# Quiz 2

#### 1. Draw a diagram of a finite-state transducer which implements the simple rewrite `'s` → ` is`.

![S-IS transducer diagram](https://raw.githubusercontent.com/yaskevich/ftyers.github.io/master/2018-komp-ling/quizzes/s-is.png)


#### 2. Give an example where your transducer expands `'s` when it shouldn't. What information could you incorporate to fix it?

Example:

>*Heavenly bound  
Cause **heaven's** got a number  
When **she's** spinning me around  
Kissing is a color  
Her loving is a wild dog  
**She's** got the look.*  
(Roxette)  

Short forms (3 person sg) of auxilary verbs TO BE and TO HAVE are neutralized in `'s`, which is not so easy to recover. We could be sure for the cases like `'s`+ Adj (e.g. *She's sad*), but other forms require more deeper parsing of the tree and, maybe, even acces to lexicon. 

#### 3. Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)

:heavy_check_mark: a) Declarative rather than procedural

:heavy_check_mark: b) Parallel application rather than sequential

:heavy_check_mark: c) More expressive than rewrite rules

:x: d) Simpler notation than rewrite rules

#### 4. What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.

**a) Using the rewrite rules without changes.**

It is impossible to use rewrite rules via copy in FS, because, for example, `hfst` ruleset is presented as hierarchical structure where we have to specify characters, lexicon and their items. 

**b) Underspecifying the rewrite rules**

We can use archiphonemes to underspecify, e.g. to deal with cases like A/O-neutralization of unstressed vowels in Belarusian. However, `hfst` seems not to be best tool to formalize stuff like this.   
```Alphabet							
в а д о у ы м 							
%{О%}:а %{О%}:о
●:0
;							
Rules							

"oa-neutralization"
%{О%}:о <=> ●:0 _ ;
```
Underspecifying allows us to produce some output which could be cut at next stages.

**c) Subtracting the context of the more general rule from the more specific
**
Rather not, it sounds logically strange, we could substract any lesser entity from a bigger one, not vice versa.

d)** Subtracting the context of the more specific rule from the more general

I guess it is like underspecifying works or, more generally, like lexicon ruleset (`hfst`) interacts with phonological one (`twolc`).

#### 5. Draw a diagram of a finite-state transducer implementing the simple English pluralization model

       SOFT = ch sh tz _s _x
       [SOFT]<PL>:[SOFT]es 
       __<PL>:__s

![pluralization transducer diagram](http://yuml.me/897d3d0e.png)


##### Implement your model in python, reading line-by-line from standard input and writing output line-by-line.

```python
import sys

for line in sys.stdin:
    word = line.rstrip()
    if word == "":
        exit()
    else:
        print(word, end="")
        if word.endswith(('ch', 'sh', 'tz', 's', 'x')):
            print("e", end="")
        print("s")
```
