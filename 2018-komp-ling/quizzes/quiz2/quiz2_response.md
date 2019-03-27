Quiz 2
1. Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".
This diagram is represented in FirstQuestion.png (according to 'Finite-State Constraints' Lauri Karttunen)

2. Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?
If we tolk about examples like "it's" it is normal to replace "'s" with "is". However if this "'s" means genetiv case  like "Sergey's book", we can check if the first letter of previous word is capital or just insert more morhpological information to te lexicon of pur transducer.   

3. Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)

a) Declarative rather than procedural +

b) Parallel application rather than sequential +

c) More expressive than rewrite rules 

d) Simpler notation than rewrite rules (+/-)

4. What strategies typically allow the rewriting of sequential rewrite rules into parallel two-level rules? Provide an example for each working strategy, and a counterexample for each non-working strategy.


    a) Using the rewrite rules without changes and d) Subtracting the context of the more specific rule from the more general. **Counterexample**:   
* Rewrite rules:   
  j → g /  _ e;   
  g → k /  _ e ;   
  **jejej → gegej → kekej**   

* Twol:    
  j:g <=> _ e ;   
  g:k <=> _ e;    
  **jejej → kekej**   



    b) Underspecifying the rewrite rules and c) Subtracting the context of the more general rule from the more specific. **Example**:   
* Rewrite rules:   
  a → b / c _ ;   
  b → d / c _ ;   
  **acaca → acbcb → acdcd**   

* Twol:    
  a:d <=> c _ ;     
  **acaca → acdcd**   
5. Draw a diagram of a finite-state transducer implementing the simple English pluralization model SOFT = ch sh tz _s _x [SOFT]:[SOFT]es __:__s

Implementation of the finite-state transducer is a script pluralModel.py. Command to use is like this: "echo 'dog<PL> and branch<PL> and lion<PL>' | python3 pluralModel.py". The result will appear in the terminal.
