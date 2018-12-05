1. ![fst1.jpg](https://github.com/DorkEMK/ftyers.github.io/blob/master/2018-komp-ling/quizzes/Quiz_2/fst1.jpg)
2. Correct:
- She's going to... - She is going to
- She's clever - She is clever
- She's a scientist - She is a scientist  
Incorrect:  
- Andy's brother - Andy is brother
- He's listened the music - He has listened the music
We can include information about part of speech (or verb form) of the next word to reduce an ambiguity
3. a, b, c
4.  
a) We can't using rewrite rules without any changes. For example (Karttunen), the rules which convert rules convert the lexical string kaNpan  to the  surface string kamman, where N is an underspecified  nasal that is realized as a labial (N:m) or as a dental (N:n)  depending on the environment, looks like:   
sequential rules:
```
(a)  N → m / _ p; elsewhere, n.
(b) p → m / m _
```
two-level rules:
```
(a) N:m  ⇔     _ p:
(b) p:m  ⇔  :m _
```
They look quite similar, but here are some differences:
- sequential rules should run in the mentioned order. Two-level rules are independent from each other and can run simultaneously
- in the case of aequential rules *m*, *p* stand for surface representation. In the second case they can state for lexical and surface level depending on the location of the colon.
 
b) Underspecification allows the rewriting of sequential rules into parallel ones. The example is overlapping harmony system in Turkish.
d) In the case than two rules contradicts each other it is possible to wubtract the context of the more specific rule from the more general, for example in Finnish, where intervocalic  k  generally disappears in the weak grade (general rule), but betvween two *u* it turns into *v* (specific rule): maku -> maun, but puku -> puvun. We can subtract the context u_u from the rule:
```
k:ε ⇐ [V - u] _ [V - u] C [#: | C]
       [V - u] _    u    C [#: | C]
       u    _ [V - u] C [#: | C]
```
c) It's hard to imagine the reverse situation, because specific rule is subpart of general rule. Subtracting general from specific leads to... nothing?

5. ![fst5.jpg](https://github.com/DorkEMK/ftyers.github.io/blob/master/2018-komp-ling/quizzes/Quiz_2/fst5.jpg)
Scrypt takes words with tag like *cat<pl>*
```
import re, sys

def pluralizer(word):
    w = ''
    if re.match('[A-Za-z]+(ch|sh|tz|s|x)\<pl\>', word):
        w = word[:-4] +'e'
    elif re.match('[A-Za-z]+\<pl\>', word):
        w = word[:-4]
    else:
        print(word + ' can\'t be pluralized')
        return
    return(w + 's')

for line in sys.stdin.readlines():
    print(pluralizer(line.strip()))
```

