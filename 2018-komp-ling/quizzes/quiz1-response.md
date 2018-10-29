# Quiz 1

1. a) b)

2. sed -e 's/\([a-z]\+\)\/\([a-z]\+\)/\1 \/ \2/g'

3. The main problem with ML techiques is that the result is sometimes hard to predict and/or understand.
I think there may be some problems with abbreviations. While in rule-based systems we can just list all the abbreviations which should be treated in a special way, in ML-systems it is not the case. For instance, imagine that in our training set there are too many examples with an abbreviation at the end of a sentence, and not so many ones with that very abbreviation in the middle of a sentence. Cf:
> They study linguistics, matematics etc. It will be useful for them.\

vs.

> They study linguistics, matematics etc. and they love it.

So, our system will learn to segment every time it finds 'etc.', and that may cause a bunch of mistakes.

4. Всемпонравилиськонинаскачках ("конина" вместо "кони на")

5. a) до н.э.\
d) Such sentences can be treated as initials:
> А.А.Иванов\
> Мама мыла раму.Рама теперь чистая.
