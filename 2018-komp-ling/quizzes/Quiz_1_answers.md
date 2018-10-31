Bakshandaeva Daria
**Quiz 1**

1. a) since MaxMatch is based on searching in the dictionary, lack of success of this algorithm may be related to the incompleteness of the dictionary (and it’s impossible to create a perfect dictionary as new words appear regularly)
   d) MaxMatch alone doesn’t care about syntactic structure of a sentence, grammatical and semantic compatibility of its elements — the algorithm just searches for the longest word in the dictionary that matches the text from the current point, no matter whether this word is connected to the previous ones or not, and how it is connected
   
2. $line =~ s/([^0-9])\\//$1 \\/ /g;
   $line =~ s/\\/([^0-9])/ \\/ $1/g;
   
3. ML is a black box in some sense: while with rule-based systems it is rather easy to understand how the system is processing, where an error is localized — thus, it’s possible to fix the error rather straightforwardly (for instance, we can add some new rules); the output of ML approach is more imprecise and the engineer can’t fully control it, some amount of new data can transform it drastically. Rule-based algorithms in some sense are more flexible (again, it’s possible to modify rules for better processing of another type of data, for example; you can involve additional databases). ML approach also requires a training corpus, which should be big enough and appropriate (and most commonly well prepared beforehand), otherwise errors are inevitable. In addition, processing large amount of data may be computationally expensive. Rule-based methods don't require such big dataset.

4. We thought she was living in a green house.

   Wet hough t shew as living in agree n house. 
   
5. a) The full stop can mark both the abbreviation and the sentence boundary: *Rome was founded in 753 B.C.* (In this particular case, for instance, if the next sentence begins with a proper name/surname, the abbreviation can be interpreted as initials).
   b) Proper names can include punctuation: *Victor Herrero, Chief Executive Officer and Director of GUESS?, Inc. stated, “As a lifestyle brand, GUESS Fragrance is and continues to be a key category for us.’’* We may also be dealing with sentences where ? or ! are considered as symbols by themselves (as in this sentence). 
   c) Separating punctuation may be missing in the data extracted from social media (informal spontaneous language samples) — and it’s pretty challenging to proceed it (without PoS-tagging, syntactic and semantic analysis): *hi let’s meet at 5 not too late ok?* Moreover, not all languages contain punctuation characters (for eхample, written Thai language). 
   d) We can also think of Thai, where space is sometimes used to mark sentence boundaries, but often there is no separation between sentences. 