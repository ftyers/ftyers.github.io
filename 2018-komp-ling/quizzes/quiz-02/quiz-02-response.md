# Quiz 2 (TBF)

### Question 1

Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".

### Answer 1

TBD

### Question 2

Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?

### Answer 2

Posessive case with 's.

We can incorporate POS-information, i.e.
* "'s" cannot be rewrited to "is" before nouns: *Nastya's repository*
* "'s" can be rewrited to "is" after verbs, determiners and all other POS: *Nastya's coding*, *Nastya's a girl* etc.

### Question 3

Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)

a) Declarative rather than procedural

b) Parallel application rather than sequential

c) More expressive than rewrite rules

d) Simpler notation than rewrite rules

### Answer 3

b), c)

### Question 4

What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules?

a) Using the rewrite rules without changes.

b) Underspecifying the rewrite rules

c) Subtracting the context of the more general rule from the more specific

d) Subtracting the context of the more specific rule from the more general

### Answer 4

b), d)

### Question 5

Draw a diagram of a finite-state transducer implementing the simple English pluralization model
```
       SOFT = ch sh tz _s _x
       [SOFT]<PL>:[SOFT]es 
       __<PL>:__s
```       
Implement your model in python, reading line-by-line from standard input and writing output line-by-line.

### Answer 5

TBD
