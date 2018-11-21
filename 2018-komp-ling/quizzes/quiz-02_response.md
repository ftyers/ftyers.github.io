##Quiz-02_response

1. Draw a diagram of a finite-state transducer which implements the simple rewrite "'s" -> " is".

2. *Give an example where your transducer expands "'s" when it shouldn't. What information could you incorporate to fix it?*

The goal of my transducer is to rewrite "'s" -> " is". Thus, cases of "'s" not being a contracted form of "is" should be omitted.

These are cases of possessive case (whose?) and contracted form of *has* (like in *Mike's literally broken his leg on stage after I told him to do so.'*.). I believe that *was* can also be contracted to "'s" in colloquial written speech.

Also, there are probably some names like O'Hara that definitely shouldn't be rewritten. O'Shara, for instance (just made it up).

**How these cases could be fixed?**

The easiest one is with names. There must be either a restriction that "s" in "'s" must be lowercase, or that "'s" must be followed by the end of the word. I believe the latter is a much better choice.

In case of a possessive case, we could check whether the previous word is capitalized. But! This would not solve the problem completely, as 
in case *"My friend Mike's kinda weird."* or *"She's super smart"* (*She* is capitalized as it's the beginning of a word.). We could also 
restrict rewriting depending on morphological characteristics of the following word. If it's a posessive case, it will be followed by a 
noun or an [adjective+noun]. Examples: *Mike's girlfriend is sweet. Mike's sweet girlfriend offered me a cup of tea.*

If it's a contracted form, it should never be 

If it is a contracted form of *has* we can see morphological characteristics of the following word. It must be a verb in III Participle form (e.g. written, got, done etc.).

3. *Which of the following are advantages of the two-level formalism for describing morphotactic rules? (Choose all that apply.)*

**a) Declarative rather than procedural**

**b) Parallel application rather than sequential**

c) More expressive than rewrite rules

d) Simpler notation than rewrite rules



