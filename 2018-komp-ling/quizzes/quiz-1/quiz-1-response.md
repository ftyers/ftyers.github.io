<!--
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

<div style="column-width: 30em">

# Quiz 1

1. Which problems does maxmatch suffer from? (Choose all that
   apply.)

      <b>a) requires comprehensive dictionary</b>
   
      <b>d) constructs non-grammatical sentences</b>

2. Write a perl/sed substitution with regular expressions that
   adds whitespace for segmentation around "/" in "either/or"
   expressions but not around fractions "1/2":
   Answer:
   
        sed 's/[[:alpha:]][/][[:alpha:]]/ \/ /'

3. the text mentions several times that machine learning
   techniques produce better segmentation than rule-based
   systems; what are some downsides of machine learning
   techniques compared to rule-based?
   Answer:
		1) model overfitting
		2) Mono-language
		3) Impossibility of interpretation

4. write a sentence (in English or in Russian) which maxmatch
   segments incorrectly.
   Answer:
   
		При правовых вопросах
    
		Приправовыхвопросах
    
		Приправ о вы х вопросах
   

5. what are problems for sentence segmentation? provide one
   example in English or Russian for each that applies.

      <b>a) ambiguous abbrevations with punctuation<b>

      <b>c) sentences lacking separating punctuation<b>

</div>
