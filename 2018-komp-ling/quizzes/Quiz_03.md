# Quiz_03
##### Anastasiya Lisitsyna
1. In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

a) Give an argument for why constraint grammar rules are more valuable.  
Constraint grammar rules are "transparent" - it is possible to find the way how mistakes occure.
b) Give an argument for why corpus annotation and HMM training is more valuable.  
Corpus annotation doesn't require as deep linguistics knowledge as rule writing, so it can be done by crowdsourcing.

Which would you prefer?
I prefer to look what resources and scills are available at the moment. I like the second way because once annotadet corpora can be used in another researches.

2. Can the two systems be used together? Explain.

Yes. HMM takes into account tokens within some window. Rules can work at the distance longer than the window width, and using rule-based system after HMM-based can improve the disambiguation.


3. Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can you do?
*Panda eats shoots and leaves*.
If disambiguator uses information about punctuation, it can possibly deal with *shoots* ambiguity. For example, rule-based sustem will require to avoid 2 verbs without comma between them. But leaves can still be a problem. n-gram HMM tagger can find *shoots and leaves* as sequence of *noun-preposition-noun* be more probable.
As for me, I can look at the context and my prior knowledge about pandas.

4. Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.

Если дизамбигуатор получает на вход токены с несколькими вариантами частеречных тегов, а на выходе каждому токену соответствует один тег, то можно оценить работу дизамбигуатора для каждого частеречного тега по отдельности при помощи следующих метрик:  
*False positive (FP)* - скольким токенам ошибочно приписан данный POS-тег  
*False negative (FN)* - скольким токенам, принадлежащим этой части речи, соответствующий POS-тег не приписан  
*Precision = TP/(TP + FP)*, где *TP - true positive* - токены, для которых дизамбигуатор правильно определил данный POS-тег. Сумма в знаменателе - скольким словам дизамбигуатор вообще приписал данный тег.  
*Recall = TP/(TP + FN)* - доля токенов, для которых правильно определён интересующий тег, среди всех токенов, которым этот тег соответствует. 
По отдельности последние две метрики лучше не рассматривать. Например, пусть на вход дизамбигуатору поступили 50 токенов, для которых один из возможных POS-тегов - NOUN, и праивльный тег NOUN - у 25 из них. Если дизамбигуатор припишет тег NOUN для всех токенов, то *FN = 0* и *Recall = 1*, и это будет выглядеть хорошо, до тех пор, пока мы не увидим, что *Precision* в этом случае равна 0.5. Можно использовать F-меру, комбинирующую обе метрики: *F = 2PR/(P+R)*.
  
Объединять результаты, полученные для каждого тега в отдельности, чтобы получить одно результирующее значение для дизамбигуатора, стоит с осторожностью.
Например, если у нас всего 10 тегов, и для 8 из них F = 0.95, а для двух - 0.6, то усреднённая F-мера получится 0.88 и замаскирует плохую работу для двух тегов.  
Кроме того, качество дизамбигуации разных тегов может иметь разную практическую значимость, и тогда можно вводить каки-нибудь взвешенные метрики.



5. Give an example where an n-gram HMM performs better than a unigram HMM tagger.
*I can empty the can.*
Unigrams *can* and *empty* are more likely to be a verb and an adjective. 