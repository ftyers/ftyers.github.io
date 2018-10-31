# 1. Which problems does maxmatch suffer from? (Choose all that apply.)
- a) requires comprehensive dictionary
- d) constructs non-grammatical sentences

# 2. Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2".
```sh
sed 's/\([a-zA-Z]\+\)\/\([a-zA-Z]\+\)/\1 \/ \2/g'  
```

# 3. The text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?
- the need of huge manually marked corpora for training
- machine learning techniques take more time to create/choose and adjust the algorithm
- machine learning techniques can sometimes have unexpected results

# 4. Write a sentence (in English or in Russian) which maxmatch segments incorrectly.
thetabledownthere -> theta bled own there

# 5. What are problems for sentence segmentation? Provide one example in English or Russian for each that applies.

- a) ambiguous abbrevations with punctuation: 
> Более 2 тыс. бутылок воды было роздано пассажирам столичной подземки и МЦК за выходные из-за жары. 

(The full stop after abbreviation "тыс." can be considered as the end of the sentence.)
- b) sentences containing symbols '!' and '?'
> "Что? Где? Когда?" — популярная телевизионная интеллектуальная игра, в которой команда знатоков в течение минуты ищет ответы на вопросы телезрителей. 

(The question marks in the title can be considered as the end of the sentence.)
- c) sentences lacking separating punctuation
> завидую крутым девочкам в тви у которых не только своя компания но и большая аудитория которая сразу пишет комменты вам через 0.5 секунд когда вы пишете твит, я чувствую себя тем самым одиноким чуваком в школьной столовке который всегда ест один

(Many examples from social media, e.g. Twitter or VK)
- d) sentences not separated by whitespace: 
> This is a test.This is a test.
