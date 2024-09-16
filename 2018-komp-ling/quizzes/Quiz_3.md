1. *a) Give an argument for why constraint grammar rules are more valuable*

CG можно использовать, когда нет большого размеченного корпуса - например с малыми языками. Также CG подходит для описания редких исключений в языке.

*b) Give an argument for why corpus annotation and HMM training is more valuable*

HMM удобно использовать для больших размеченных данных, это достаточно продуктивно и занимает меньше времени, чем CG.

2. Да, конечно, две системы могут работать вместе. Например, сначала с помощью constraint grammar можно убрать все невозможные теги, а потом выбрать верный с помощью HMM.

3. 

4. False positive - ответы, отмеченные как правильные, но на самом деле они не правильные. True positive - это правильные ответы, отмеченные как правильные.

   False negative -  ответы, на самом деле являющиеся правильными, но отмеченные как неверные. True Negative - неверные ответы отмеченные как неверные.

   Precision = True Positive/(все ответы отмеченные как Positive);

   Recall = TP/(TP+FN). 

5. *Give an example where an n-gram HMM performs better than a unigram HMM tagger*

