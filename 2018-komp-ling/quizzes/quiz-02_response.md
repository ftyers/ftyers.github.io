##Quiz-02_response

1. Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".

*See quiz_02-1.png*

2. *Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?*

The goal of my transducer is to rewrite "'s" -> " is". Thus, cases of "'s" not being a contracted form of "is" should be omitted.

These are cases of possessive case (whose?) and contracted form of *has* (like in *Mike's literally broken his leg on stage after I told him to do so.'*.). I believe that *was* can also be contracted to "'s" in colloquial written speech.

Also, there are probably some names like O'Hara that definitely shouldn't be rewritten. O'Shara, for instance (just made it up).

**How these cases could be fixed?**

The easiest one is with names. There must be either a restriction that "s" in "'s" must be lowercase, or that "'s" must be followed by the end of the word. I believe the latter is a much better choice.

In case of a possessive case, we could check whether the previous word is capitalized. But! This would not solve the problem completely, as 
in case *"My friend Mike's kinda weird."* or *"She's super smart"* (*She* is capitalized as it's the beginning of a word.). We could also 
restrict rewriting depending on morphological characteristics of the following word. 

If it's a posessive case, it will be followed by a [noun] or an [adjective+noun]. 

Examples: *Mike's girlfriend is sweet. Mike's sweet girlfriend offered me a cup of tea.*

If it is a contracted form of *has* we can see morphological characteristics of the following word. It must be a verb in III Participle form (e.g. written, got, done etc.) or with "-ed" ending.

**Overall:** The best way to define whether "'s" should be replaced by "is" - see the morphological characterictics of the following word. It should be a gerund (*Mike's speakING*), an adverb (*Mike's definiteLY late*), an article (*Mike's a guy I told you about*). 

**NB!** If a previous word is a pronoun (*He's kind.*) and the following (or a word after) word is not a 3rd Participle or "-ed" ending (*He's done it. = 'has'*; *He's kindly offerED me a cup of tea.*),"'s" should be replaced by "is".

It's a bit more difficult with adjectives, for instance: "*Mike's kind and generous*" VS "*Mike's kind sister offered me tea*". Here we should ckeck whether there are any nouns ahead that our adjective relates to.

3. *Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)*

**a) Declarative rather than procedural**

**b) Parallel application rather than sequential**


4. *What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.*

a) Using the rewrite rules without changes.

*Contrexample:* As was mentioned in our tutorial, parallel rules are applied at the same time. That is why rewriting formal approach rules would break everything:

| formal approach | hfst          |
|-----------------|---------------|
| a → b / c _ ;   | b → d / c _ ; |
| b → d / c _ ;   | b:d <=> c _ ; |
|acaca → acbcb → acdcd|acaca → acbcb|

**b) Underspecifying the rewrite rules**

*Example from Finnish*
```
(a) k:v <=> u _ u C [#: | C]
(b) k:[epsilon] <= V _ V C [#: | C]
```
Without ordering, (a) and (b) are in conflict. To sort it out, we can perform the following:
```
(c) k:[epsilon] | k:v <= V _ V C [#: | C]
```

c) Subtracting the context of the more general rule from the more specific

*Counterexample:*
```
(a) N -> m / _ p ; 
(b) p -> m / m _ ;
```
Here kaNpan can't be realized as kampton

**d) Subtracting the context of the more specific rule from the more general**

*Example from chv.lexc*
```
"%{Ă%}:0 if there is previous %{м%}: or a vowel and, optionally, a following н"
%{Ă%}:0 <=> %{м%}: %>:  _ н ;
	          Vowels: %>: _ ; 

"%{м%}:0 if there is a following %{Ă%}: followed by н"
%{м%}:0 <=> _ %>: %{Ă%}: н ;
```
5. Draw a diagram of a finite-state transducer implementing the simple English pluralization model

*See quiz_02-5.png*

*Implement your model in python, reading line-by-line from standard input and writing output line-by-line.*
```
import sys
import re

soft = ['ch', 'sh', 'tz', 's', 'x']

for line in sys.stdin.readlines():
  if re.search(str([i for i in soft])+'<PL>', line):
	  line = line.replace('<PL>','es')
		print(line)
	else:
		line = line.replace('<PL>','s')
print(line)
```

