<!--
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)

-->

<div style="column-width: 30em">

# Quiz 3

1.	In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.
	
  a)	Give an argument for why constraint grammar rules are more valuable
  
  <b>Constraint grammar rules gives us a great precision score, but a recall score is low most of the time. 
  So, if constraint rules can be simple implemented – we should use constraint grammar. </b>
	
  b)	Give an argument for why corpus annotation and HMM training is more valuable
  
  <b>Counterwise, HMM gives us a great Recall score (bigger than CG rules), 
  but  HMM will never reach the Precision level of CG rules</b>


2. Can the two systems be used together? Explain.

  <b>Yes. The basis of the grammar is composed of constraint rules. Yet, when rules
  cannot provide a solution, there is room for the use of elements that contain
  probabilistic features; this contributes to robustness in the grammar. 
  So, first of all we should use CG rules, and after that – HMM.</b>

3.	Give a sentence with morphosyntactic ambiguity. 
What would you expect a disambiguator to do in this situation? What can you do?


<b>‘Косой косой косил косой’</b>

In this case disambiguator will give us 

    [A,A,V,N]
  
because for a verb there must be a NOUN. 
But the real PoS tags are 

    [A,N,V,N]
  
4.	Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, 
and describe how to compute them. Describe what it would mean to have disambiguators which 
differ in quality based on which quantity is used.

  Difficulty in evaluate the proper score for FP,FN e.t.c is what we need to summarize 
  all the answers for every tag we have. Example: take all NOUN tag from golden standard 
  and from the answers of our model. If :

•	Standard and answers equal = TP

•	Standard is NOUN, but answer is not = FN

•	Answer is NOUN, but standard is not = FP

•	Not Standard, nor answer is NOUN = TN

Next, we summarize all answers and calculate Precision and Recall.

5.	Give an example where an n-gram HMM performs better than a unigram HMM tagger.

</div>
