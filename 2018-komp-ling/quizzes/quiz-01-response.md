# Quiz 1

## Question 1

Which problems does maxmatch suffer from?

Answer:

a) requires comprehensive dictionary

b) is computationally expensive

d) constructs non-grammatical sentences

## Question 2

Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2":

Answer: sed -e 's/\([a-z]\+\)\/\([a-z]\+\)/\1 \/ \2/g'

## Question 3

The text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?

1) Machine learning techniques usually need much data to be trained.
2) Training data can be messy.

## Question 4

Write a sentence (in English or in Russian) which maxmatch segments incorrectly.

Answer:

"арозаупаланалапуазора"

Верно: "а роза упала на лапу азора"

vs.

Неверно: "ар о за упала на лапу азора"

## Question 5

What are problems for sentence segmentation? Provide one example in English or Russian for each that applies.

Answer:

a) ambiguous abbrevations with punctuation

	Путин В.В. -- президент РФ.

b) sentences containing symbols '!' and '?'

	"Это ты сделал, Иванов? Выйди вон!", -- воскликнул преподаватель.

c) sentences lacking separating punctuation

	привет как дела (this should be 2 different sentences "привет" and "как дела")

d) sentences not separated by whitespace

	тыктотакойдавайдосвидания (this should be 2 different sentences "ты кто такой" and "давай до свидания")