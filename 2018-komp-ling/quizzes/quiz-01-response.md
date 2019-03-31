# Quiz 1

## Question 1

Which problems does maxmatch suffer from?

Answer:

a) requires comprehensive dictionary

b) is computationally expensive

d) constructs non-grammatical sentences

## Question 2

Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2":

Answer:

sed -e 's/\([a-z]\+\)\/\([a-z]\+\)/\1 \/ \2/g'

## Question 3

The text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?

1) Machine learning approaches usually need much data to be trained and training data for its part can be messy.
2) Maching learning approaches often work like a "black box" and their results can be difficult to interpret.

## Question 4

Write a sentence (in English or in Russian) which maxmatch segments incorrectly.

Answer:

"арозаупаланалапуазора"

Right segmentation: "а роза упала на лапу азора"

vs.

Wrong maxmatch segmentation: "ар о за упала на лапу азора"

## Question 5

What are problems for sentence segmentation? Provide one example in English or Russian for each that applies.

Answer:

a) ambiguous abbrevations with punctuation

	Путин В.В. был президентом РФ в 2000-2008 гг. и является президентом РФ с 2012 г. по н. вр.

b) sentences containing symbols '!' and '?'

	"Это ты сделал, Иванов? Немедленно выйди вон!" -- воскликнул преподаватель.

c) sentences lacking separating punctuation

	привет как дела (this should be 2 different sentences "привет" and "как дела")

d) sentences not separated by whitespace

	ты кто такой?давай до свидания! (this should be 2 different sentences "ты кто такой" and "давай до свидания")
