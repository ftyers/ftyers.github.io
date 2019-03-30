#### 1. Which problems does maxmatch suffer from? (Choose all that apply.)

**Answer**: \
**a)** requires comprehensive dictionary\
**b)** is computationally expensive  (as when we use a comprehensive dictionary, going over it again and again to find the word might be computationally expensive if the dictionary is large)\
**d)** constructs non-grammatical sentences

#### 2. Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2"

 "either/or" -> "either / or"\
 "1/2"       -> "1/2"

**Answer**: sed -e 's/\([a-z]\+\)\/\([a-z]\+\)/\1 \/ \2/g'

#### 3. The text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?

**Answer**: 
+ machine learning tecniques require a large dataset in order to train a good enough segmentating model; although, even then the model would have a hard time catching all of the cases for segmentation.
+ rule-based, however, is easier to control as a person can observe the data to write a comprehensive set of rules for out-of-ordinary cases. 

#### 4. Write a sentence (in English or in Russian) which maxmatch segments incorrectly.

**Answer**: \
"The construction was underdeveloped", as maxmatch would output "The construction was under developed".

#### 5. What are problems for sentence segmentation? provide one example in English or Russian for each that applies.

**Answer**:\
**a)** ambiguous abbrevations with punctuation\
"Mr. Green asked Ms. Grey if she had met Dr. Jekyl."\
**b)** sentences containing symbols '!' and '?'\
‘Just a moment!’ she shouted.\
‘Can I come in?’ he asked.\
**c)** sentences lacking separating punctuation\
I work at Sleeman Breweries Ltd. Before that, I worked in the automotive industry.
