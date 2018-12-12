Funny story: after I made this quizz something happened with branches and I couldn't switch to master branch in GitHub desktop
and there were some strange changes in another folder, so it happened that all my works were deleted from my computer
and I wrote everything again out of my memory, so I'm sorry if the answers are too short or smth............................


1. a) No need in large human-annotated corpora.  
b) Model distribution, tagsets learnt from the data.  
I'd prefer rules.

2. We can at first remove the impossible tag possibilities for words using rule-based approach and the use HMM to choose the best sequence.  

3. _Time flies like an arrow._
Disambiguator will choose between NOUN and VERB for "Time", between NOUN and VERB for "flies", between NOUN, VERB and PREP
for "like". I could write some simple rules, stating that, for example, when after word there is 3rd person verb, singular noun
tag should be chosen and the opposite for "flies", then I can write a rule that PREP should be chosen before determiner and after
verb. (Of course rules should be more complicated...)

4. FP - predicted positive, but really negative, unlike True Positive; FN - predicted negative, but really positive, unlike True Negative. Precision = TP/(TP+FP); Recall = TP/(TP+FN).  
For disambiguation task I guess FPs are tags that were chosen by algorithm, but are incorrect; and FNs are the right tags that were not chosen by the algorithm (?? strange, probably I don't understand the question clearly). Precision - how much of the right tags were chosen correctly, recall - how much right tags were predicted at all (strange again).

5. I think the previous example (from 3) is suitable, especially for the word _flies_.
