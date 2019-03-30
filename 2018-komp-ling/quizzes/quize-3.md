1.  a) Constraint grammar rules are the only way for the languages with no available annotated corpora. Moreover, while the rules are described explicitly, it's easier to debug. 
    
    b) Corpus annotation and HMM training requires a lot of annotation work but after it's done, we can use it in a variety of tasks. Moreover, you don't need to have a deep knowledge in linguistics or to know everything about specific language. 
    
    Preference for a particular approach is based on the task and on the data we have (or we could have). For example, for languages with no available annotated corpora it's only rule-based way. For languages with lots of corpora, we can implement some HMM but sometimes it could be an overkiller. 

2. Of course, this two systems could be used together. We can correct HMM-made mistakes using the rules or make some annotation using the rules and then train our model.

3. _Солнце село за горизонт_

 _село_ is the verb(3NPST) but it could be annotated as the noun. We can add some rules like _if the previous token is a noun with the same gender as marked in this ambigous case, let's say it's a verb_.
 
 4. false positive - cases, when, for example, tagger marked a word with the wrong tag (in comparison with the gold standard)
 false negative - caes, when tagger didn't give a word a tag which it should give based on the standard
 precision - a number of correct answers devided by all the results 
 
 5. _Visa applications take 28 days to process._
 
 The word _process_ is more frequently used as a noun, so unigram HMM tagger could label it as a noun, while it doesn't take context into account.
