# 1

See file quiz-02-task-01.bmp.

# 2

E. g. "Vadim's homework is awesome" would be transduced to "Vadim is homework is awesome". Maybe we could use morphological tags to disambiguate here.

# 3

a, b

# 4
a - not working, e. g. this example from Karttunen that describes the pronounciation of the words
writer and rider in Canadian English:

```
(a)	ay -> &y / _ -V
(b)	t,d -> D / V _ V
```

```
(a)	ay:&y <= _ -V:
(b)	t:D | d:D <= V _ V
```
Here, the rules are not parallel since the result of their application depends
on the order in which they are applied.

b - working, e. g. for describing vowel harmony in Turkish:

```
Rounding Harmony
	HiHrmVowel:HiRndVowel <=> :RndVowel :C* _

Back Harmony
	Vx:Vy <=> :BackVowel :C* _ ;
	where Vx in (HiHrmVowel LowHrmVowel)
	      Vy in (HiBackVowel LowBackVowel) matched [14]
```

Here, neither of the rules in specific enough to cover any specific case, but their combination covers all possible cases correctly.

c - working, e. g. for Finnish:

turning 
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C]
```
into
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C]
       			[V - u]	_ u C [#: | C]
			      u	_ [V - u] C [#: | C]

d - working, e. g. for Finnish:

turning 
```
(a)	k:v <=> u _ u C [#: | C]
(b)	k:[epsilon] <= V _ V C [#: | C]
```
into
```
(a)	k:v <=> u _ u C [#: | C]
(b)		k:[epsilon] | k:v <= V _ V C [#: | C]
```
This shuts off the possibility of applying (b) where (a) is applicable, to the context of the specific rule is now subtracted from the contest of the general one.

