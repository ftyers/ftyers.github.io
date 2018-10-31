1. Which problems does maxmatch suffer from? (Choose all that apply.)
      
      *a) requires comprehensive dictionary
      d) constructs non-grammatical sentences*

2. Write a perl/sed substitution with regular expressions that
   adds whitespace for segmentation around "/" in "either/or"
   expressions but not around fractions "1/2":

        "either/or" -> "either / or"
        "1/2"       -> "1/2"
        
    ```sed 's/\([^0-9]\+\)\/\([^0-9]\+\)/\1 \/ \2/g'```

3. the text mentions several times that machine learning
   techniques produce better segmentation than rule-based
   systems; what are some downsides of machine learning
   techniques compared to rule-based?

    *Machine-learning techniques are often harder to interpret (e.g. all these NN-based solutions). Having found the group of mistakes produced by the ML-algorithm you won't just add a bugfix cause the whole model needs to be rebuilt and retrained.*
4. write a sentence (in English or in Russian) which maxmatch
   segments incorrectly.
   
   *An ambigous example from the school textbook: "наполеонсеялрожь". Maxmatch will choose the less statistically probable examle "наполеон сеял рожь".*

5. what are problems for sentence segmentation? provide one
   example in English or Russian for each that applies.

      a) ambiguous abbrevations with punctuation
      
        *"... и т.п. случаи"*
        
      b) sentences containing symbols '!' and '?'
      
        "Are you O.K.?!"
        
        "Here ```!condition ? do_this_if_inverted_condition_is_true : do_that_if_inverted_condition_is_false``` is the ternary operator usage example"
        
      c) sentences lacking separating punctuation

      d) sentences not separated by whitespace
