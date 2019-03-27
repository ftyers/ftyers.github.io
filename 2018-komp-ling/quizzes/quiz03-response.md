## Quiz 3

1. a) It seems to me that if constraint grammar rules are quite accurate and cover considerable amount of cases, they work more precisely than ML technique. Moreover, with rule-based approach an engineer has an opportunity to understand what is going on or why something does not work, and just add or delete rules. And with ML approach it is always some kind of magic inside which you can not always predict.

   b) I guess that for building a constraint grammar we need to know well the language in question, otherwise there is a chance to generate some wrong rules. Thus, training approach seems easier, as one does not need to have profound knowledge in the language under consideration.
I would prefer HMM training, because creating constraint grammar rules seems quite difficult and requires special knowledge.

2. Yes, we can write some constraint grammar rules to implement after training to fix some mistakes made by the algorithm. For instance, HMM algo may not cover some named entities or abbreviations.

3. _Мама мыла раму_

A disambiguator would choose an interpretation with higher probability score (if we use HMM), and I guess it would assign tag **V** to _мыла_, although a unigram-tagger may as well parse _мыла_ as a form of noun _мыло_. If we use constraint grammar rules, we can state a rule that if a word is situated between 2 nouns, one of which is in Nominative case, this word is a verb.

4. **Accuracy**: given the size of sample N, A = V / N, where V is the number of correct tags. We consider a tag as a correct one if all parts of a tag are ascribed correctly (part of speech, case, number, gender)

If all parts of a tag are correct, we consider the case as True Positive (tp) one. Let us say that if part of speech was ascribed incorrectly we assume that the case to be False Negative (fn). If part of speech was determined correctly, but case and/or number and/or gender were predicted incorrectly, than it is a False Positive (fp) case. Therefore: 

 **Precision**: tp / (tp+fp).
 
 **Recall**: tp / (tp+fn). 
 
If two disambiguators differ in accuracy, that means that one of them just works more precisely than the other. As for precision, we can say that one of the disambiguators predicts parts of speech better, and in case of recall we can conclude that a disambiguator is more "fine-grained" as it is able to determine bettter such details as case or gender.

5. _To book a flight_

If we use a unigram tagger, _book_ would be parsed as a noun, while in case of an n-gram tagger particle _to_ would indicate that we are dealing with a verb. So, an n-gram tagger would perform better.
