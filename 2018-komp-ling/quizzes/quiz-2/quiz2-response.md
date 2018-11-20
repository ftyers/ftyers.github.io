# Quiz 2 by Nikolaeva Anna

1. See fst1.jpg. "<n>" stands for a noun, ">" stands for the morpheme boundary, "0" stands for nothing on the surface. In this transducer we have some input noun with suffix "'s", and in the output we have a surface space in the place of the morpheme boundary and the apostrophe becomes "i".
2. Examples:
- geese's → geese is (incorrect)
- Cate's house → Cate is house (incorrect)

For fixings the mistakes of the second type, we should look at the morphological disambiguation level, and that, as far as I understand, cannot be done within FSTs or it is rather elaborate. 

But we can deal with the first type of mistakes (geese's → geese is). Apparently we should make some changes on the morphotactic side of our transducer in a way that we expand "'s" only when it goes after the noun in a singular form. Then the transducer might look like fst2.jpg. 

3. a, b, c 
4. 
a) To my mind, it's not possible to rewrite rewrite rules into parallel two-level rules without changing them, as in FSTs there is not only input (lexical) level, but also a surface level, so there will always be the difference in a way the rule looks like (in two-level rules there is a ":" used to show the transducer from lexical side to surface, and two-level rules have more operators, than rewrite rules). For example, for the following two rewrite rules, which convert the lexical string "kaNpan" to the surface string "kamman":  
```
(a)	N -> m / _ p; elsewhere, n.
(b)	p -> m / m _
```
the two-level rules will look like that:
```
(a)	N:m <=>    _ p:
(b)	p:m <=> :m _
```
They look similar, but in the first case 'p' and 'm' on the right belong only to the input level, and in the second case 'p:' belongs to the input level and ':m'belongs to the output (surface) level, and exactly that allows us to apply these rules parallelly to get the right output. 

b) We can use underspecification to rewrite rewrite rules into parallel two-level rules. For example, we can apply the following rewrite rules according to their order to get the output of the Finnish genitive 'maku' (taste) as 'maun', but the genitive of 'puku' (dress) as 'puvun':
```
(a)	k -> v / u _ u C (C) #
(b)	k -> ∅ / V _ V C (С) #
```
But we cannot rewrite them into two-level rules as: 
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C],	
```
because they will get in conflict with one another. But we can use a symbol "|" (the logic "or") to make a correspondence part of the rule broader in the second rule (to "underspecify" the rule):
```
(a)	k:v <=> u _ u C [#: | C]	
(b)	k:[epsilon] | k:v <= V _ V C [#: | C]	
```
c) I don't understand the meaning of subtracting the context of the more general rule from the more specific. 
For example, the rewrite rule from the answer (b) 
```
k -> v / u _ u C (C) # 
```
is already specific. In two-level rules we cannot write anything like 
```
k:[epsilon]  <=> [u - V] _ [u - V] C [#: | C]	
```
in order to get 'maun' from 'maku', but 'puvun' from 'puku'.  "[u - V]" seems to be nonsence. 

d) Theoretically we may subtract the context of the more specific rule from the more general rule to make the general two-level rule more specific, but it is not an optimal solution. We can try to rewrite the rewrite rules from the answer (b) as:
```
k:[epsilon] <=	[V - u]	_	[V - u] C [#: | C]
       		    [V - u]	_	u C [#: | C]
       		    u	_	[V - u] C [#: | C]
```
But it looks complicated. In this case we may always resort to underspecification to make two-level rules simplier. 

Or maybe we can use the 'except' syntax in a twol file to subtract the context of the specific rule, that contradicts to our general rule. 

5. See fst3.jpg. I have tried to draw it as I understand it. Again, > stands for a morpheme boundary. "Other" stands for all other cases not included in SOFT. 
My code can be seen in plural.py. It will work with input as in nouns.txt. 






