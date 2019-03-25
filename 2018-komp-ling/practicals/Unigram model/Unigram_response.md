\documentclass{article}
\usepackage[utf8]{inputenc}

\title{Unigram models}
\author{Nikolay Babakov }
\date{November 2018}

\begin{document}

\maketitle

\section{Creating necessary file}
I used the data from previous assignment, copied some sentnces parsed with conluu file. 

Then I implemented some functions which will help me with the whole task
Function go_over_dict_val 
iterate iver dict and return all keys and values inside the dict

Function tags_calc
Iterate over collected tags and create a unit which has all necessary items for output
The functon returns list of units

Function word_calc
We cretae word tag dictionary, which has one ore more another dictionary inside it. The structure is namely word - tag - word_taf_frequency. In case of multitag word there will be two ot more dictionaries insode one dictionary
The functon also returns list of units

Then we concatenate two lists and write tem into unigram.txt
The file is inside the repo

\end{document}

What might be a simple improvement to the language model for languages with orthographic case ?

We can simply preprocess the text using tolower function so word will be the ame regardless its position in a sentence.
