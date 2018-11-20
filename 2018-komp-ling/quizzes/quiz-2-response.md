# Quiz 2

1. Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".

2. Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?

The transducer expands "'s" in such cases as "Mike's" or "Ana's". To avoid this situation, we should specify that the change should only be happening when this "'s" does not state the posessive case.

3. Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)

    **a) Declarative rather than procedural**

    **b) Parallel application rather than sequential**

    c) More expressive than rewrite rules

    *d) Simpler notation than rewrite rules*

4. What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.

    a) *Using the rewrite rules without changes and d) Subtracting the context of the more specific rule from the more general*. **Counterexample**:   
* Rewrite rules:   
  a → b / c _ ;   
  b → d / c _ ;   
  **acaca → acbcb → acdcd**   

* Twol:    
  a:b <=> c _ ;   
  b:d <=> c _ ;    
  **acaca → acbcb**   

    b) *Underspecifying the rewrite rules and c) Subtracting the context of the more general rule from the more specific*. **Example**:   
* Rewrite rules:   
  a → b / c _ ;   
  b → d / c _ ;   
  **acaca → acbcb → acdcd**   

* Twol:    
  a:d <=> c _ ;     
  **acaca → acdcd**   

5. Draw a diagram of a finite-state transducer implementing the simple English pluralization model
   
```
       SOFT = ch sh tz _s _x
       [SOFT]<PL>:[SOFT]es 
       __<PL>:__s
```

```
import sys
import re

dictn = {'ch<PL>':'ches', 'sh<PL>':'shes', 'tz<PL>':'tzes', 's<PL>':'ses', 'x<PL>':'xes'}

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    text = re.sub('<PL>', 's', text)
    return text

for data in sys.stdin:
	res = replace_all(data, dictn)

print(res)
```
