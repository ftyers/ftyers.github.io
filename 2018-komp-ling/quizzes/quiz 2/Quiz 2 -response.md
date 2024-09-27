# Quiz 2

1. Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".
- See 1_transducer.jpg in the folder.
2. Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?
- My transducer does expand "'s" when it is a posessive case: *dog's bone*, *Kate's dress*. So we should add a morphological rule that says that "'s" shouldn't be followed by a noun. 
- Correct context should be the following: 
--"'s" is followed by a verb/verb form *Dog's walking*, 
--"'s" is followed by a preposition *Dog's at home*,
-- "'s" is followed by an adverb *Dog's there*,
-- "'s" is followed by an article *It's a dog*,
-- "'s" is followed by a pronoun *It's my dog*,
--"'s" is followed by an an adjective *Dog's cute*. However there is an exception in this rule if we have *Kate's beautiful dress* which can be incorrectly expanded into *Kate is beautiful dress*. It means that the adjective which is following "'s" should not be followed by a noun.

3. Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)

- a) Declarative rather than procedural
- b) Parallel application rather than sequential


4. What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.
- Doesn't work: a) Using the rewrite rules without changes.
```
j -> h / _ a;
h -> l / _ a;
jajaja -> hahaha -> lalala
```

- Works (example from Karttunen) b) Underspecifying the rewrite rules
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C]
```
- Doesn't work(example from Karttunen): c) Subtracting the context of the more general rule from the more specific
```
(a)	N -> m / _ p; elsewhere, n.
(b)	p -> m / m _
```
kaNton cannot be realized as kamton

- Works (example from Karttunen) d) Subtracting the context of the more specific rule from the more general
```
k:[epsilon] <=	[V - u]	_	[V - u] C [#: | C]
       		[V - u]	_	u C [#: | C]
       		      u	_	[V - u] C [#: | C]

```
5. Draw a diagram of a finite-state transducer implementing the simple English pluralization model
- See 1_transducer.jpg in the folder.

       SOFT = ch sh tz _s _x
       [SOFT]<PL>:[SOFT]es 
       __<PL>:__s
Implement your model in python, reading line-by-line from standard input and writing output line-by-line.
- See pluralization.py in the folder
Instruction:
- run in terminal using *python3 pluralization.py*
- type the word you want to pluralize (no exceptions!)