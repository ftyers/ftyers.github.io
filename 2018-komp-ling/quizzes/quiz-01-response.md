<!--
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

<div style="column-width: 30em">

# Quiz 1

1. Which problems does maxmatch suffer from? (Choose all that
   apply.)
   Answers: a, d

      a) requires comprehensive dictionary
      d) constructs non-grammatical sentences

2. Write a perl/sed substitution with regular expressions that
   adds whitespace for segmentation around "/" in "either/or"
   expressions but not around fractions "1/2":
   
   
   Answer: sed 's/\([^0-9]\+\)\/\([^0-9]\+\)/\1 \/ \2/g'

        "either/or" -> "either / or"
        "1/2"       -> "1/2"

3. the text mentions several times that machine learning
   techniques produce better segmentation than rule-based
   systems; what are some downsides of machine learning
   techniques compared to rule-based?
   
   You have to train your algorithm, which takes time and large 
   amounts of data, and even then you can apply your algorithm
   for a particular language only. Also you can't always know how
   exactly the algorithm works, so it's hard to correct its work
   in case it works incorrectly. The results are hard to interpret.
   You have to figure out how to measure the efficiency and compare
   you results to results of other techniques and algorithms.

4. write a sentence (in English or in Russian) which maxmatch
   segments incorrectly.
   text: andlilywouldtellmenoandmakeupthemostridiculousexcuses
   maxmatch: and lily would tell meno and makeup them ost ridiculous excuses
   reference: and lily would tell me no and makeup the most ridiculous excuses

5. what are problems for sentence segmentation? provide one
   example in English or Russian for each that applies.

      a) ambiguous abbrevations with punctuation
      	e.g.

      b) sentences containing symbols '!' and '?'
      	Yahoo!

      c) sentences lacking separating punctuation
      	I cannot tell you it's confidential 
      	# although it could be one sentence separated by a comma

      d) sentences not separated by whitespace
	  	The first sentence.The second sentence
</div>
