## Quiz 2

### Vladislav Mikhailov MKL181

1. *Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".*

![1](2quiz1.jpg?raw=true)

2. *Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?*

The transducer can expand "'s" when not needed:
* contracted form of the pronoun *us*, e.g. *let's have fun with HFST*:
	* we need to introduce the information of the word "'s" attached to – the verb "let";
* contracted form of the auxiliary verb *has*, e.g. *she's gone away*:
	* we need to introduce the morphological features of the word following "'s" – verb, participle 2 or ending "ed";
* some names, e.g. *O's Pasta is a cafe*;
	* we need to introduce the morphological features of the word following "'s" – it shouldn't be a proper noun;
* possessive case, e.g. *Mary's friend*:
	* we need to introduce the morphological features of the word following "'s" – it should be a noun or a noun phrase (adj + n).

The transducer should expand "'s" when:
* the following word is a gerund, e.g. *Jack's reading a book*;
* the following word is an article, e.g. *she's a doctor*, *it's the best film*;
* the following word is a possessive pronoun, e.g. *it's my sister*;
* the following word is a pronoun, e.g. *it's me*;
* the following word is a demonstrative pronoun, e.g. *it's this*, *it's that*.
* when the following word is a negative particle *not*, we need to combine the five cases so that to expand *'s* to *is*, e.g. *it's not that simple -> it is not that simple*, *she's not you -> she is not you*.

3. *Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)*

**a) Declarative rather than procedural**

**b) Parallel application rather than sequential**

4. *What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.*

**a) Using the rewrite rules without changes.**

*Contrexample:* doesn't work, since parallel rules are applied at the same time.

* rewrite rules:
k -> n / _ i ;
n -> m / _ i ;
**kikik -> ninin -> mimim**
* twol:
k:n <=> _ i ;
n:m <=> _ i ;
**kikik -> mimim**

**b) Underspecifying the rewrite rules and d) Subtracting the context of the more specific rule from the more general**

*Example from Karttunen*
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C]
``` 
Without ordering, the rules are in conflict. The solution is to impose an order on the rules:
``` 
k:[epsilon] | k:v <= V _ V C [#: | C]	
```

**c) Subtracting the context of the more general rule from the more specific**
*Counterexample:*

*Example from Karttunen*
``` 
(a)	N -> m / _ p; elsewhere, n.
(b)	p -> m / m _
``` 

5. *Draw a diagram of a finite-state transducer implementing the simple English pluralization model*

![5](2quiz2.jpg?raw=true)

How to use:
```
$ python3 quiz2.py < <filename>
```

Implementation:
```
import re
import sys


soft = {'ch<PL>':'ches', 'sh<PL>':'shes', 'tz<PL>':'tzes', 's<PL>':'ses', 'x<PL>':'xes'}
for line in sys.stdin.readlines():
    lines = line.strip()
    for key, value in soft.items():
        lines = lines.replace(key, value)
    lines = re.sub('<PL>', 's', lines)
    print(lines)
```

Example:
```
$ python3 quiz2.py < test.txt

std input:
glitch<PL>, kiss<PL>, quartz<PL>
box<PL>, dash<PL>, apple<PL>, dog<PL>

std output:
glitches, kisses, quartzes
boxes, dashes, apples, dogs
```