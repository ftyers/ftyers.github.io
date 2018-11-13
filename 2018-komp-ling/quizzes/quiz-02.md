<!--
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

<div style="column-width: 30em">

# Quiz 2

1. Draw a diagram of a finite-state transducer which implements
   the simple rewrite "'s" -> " is".

2. Give an example where your transducer expands "'s" when it
   shouldn't. What information could you incorporate to fix it?

3. Which of the following are advantages of the two-level
   formalism for describing morphotactic rules? (Choose all that
   apply.)

    a) Declarative rather than procedural

    b) Parallel application rather than sequential

    c) More expressive than rewrite rules

    d) Simpler notation than rewrite rules

4. What strategies typically allow the rewriting of sequential
   rewrite rules into parallel two-level rules? Provide an
   example for each working strategy, and a counterexample for
   each non-working strategy.

    a) Using the rewrite rules without changes.

    b) Underspecifying the rewrite rules

    c) Subtracting the context of the more general rule from the
       more specific

    d) Subtracting the context of the more specific rule from the
       more general

5. Draw a diagram of a finite-state transducer implementing the simple English
   pluralization model
```
       SOFT = ch sh tz _s _x
       [SOFT]<PL>:[SOFT]es 
       __<PL>:__s
```

   Implement your model in python, reading line-by-line from standard input and
   writing output line-by-line.
      

</div>
