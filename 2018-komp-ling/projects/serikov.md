# Compling project proposal

## Abstract
**TO-DO** one-paragraph summary of the rest of the proposal.

## Introduction
**TO-DO** the background of the problem to be solved or topic to be studied, with references for the low-background reader.
RE: extracting phonological rules from neural networks paper: Jennifer Rodd (1997) "Recurrent Neural-Network Learning of Phonological Regularities in Turkish". CoNLL97: Computational Natural Language Learning, http://www.aclweb.org/anthology/W97-1012

Задача интерпретации нейронных сетей хорошая, добрая. Задача применения машинного обучения для извлечения интересных с точки зрения лингвистики данных хорошая, добрая.

Статья (статья) показывает подход к решению поставленных задач, опробованный на турецком языке. Интересно проверить описанные в статье подходы на других языках, особенно на родственных рассмотренному в статье турецкому.

Параллели в фонетических свойствах между родственными языками было бы интересно попробовать применить к исследованию фонетических эмбеддингов в родственных языках.

## Proposed goals

### MVP
* Re-implement the paper
* Release the code and documentation showing how to run it
* Extract the graphs that are contained in the original paper

### EP
Run the NNs explored in the original paper with other languages in the Turkic family to see if their networks split the same way (other Turkic languages have different vowel harmony systems, and Uzbek does not have vowel harmony at all). 

### HAP
Apply the received knowledge of computational phonology and Turkic family languages phonology in particular to solve the task of phonetic embeddings alignment without having big parallel corpus.

## Requirements

**NB!** Each sub-goal is accompanied with the documentation composing and sources publishing where needed.

**NB!** Goals may be changed on the run if necessary (e.g. smth unexpected discovered). All the possible changes should be discussed with mentors.

### MVP requirements
#### Skills required
* Brief knowledge of actual NN creating techniques.
* Data preprocessing skills
* Vizualization skill.

#### Sub-goals (~ 21 nov &ndash; 15 dec 2018)
* 1 week (21 &ndash; 27 nov 2018) Reproduce the dataset used in original paper
* 1/2 week (28 &ndash; 30 nov 2018) Reproduce the NNs used in original paper
* 1/2 week (1 &ndash; 4 dec 2018) Reproduce the training process used in original paper
* 1/2 week (5 &ndash; 7 dec 2018) Reproduce the NNs analysis described in original paper
* 1/4 week (8 &ndash; 9 dec 2018) Compare the reproduced and original results
* 1/4 week (10 &ndash; 11 dec 2018) Draft the results report
* 1/4 week (12 &ndash; 13 dec 2018) Discuss the results with mentors
* 1/4 week (14 &ndash; 15 dec 2018) Report the results of the MVP stage online (e.g. repo readme)

### EP requirements

#### Sub-goals (~ 16 dec 2018 &ndash; 15 jan 2019)
* 1 week (d-d m y) Collect the data to repeat the research on different languages data
* 1/4 week (d-d m y) Accomplish the ML part of the research
* 1/2 week (d-d m y) Accomplish the analysis part of the research
* 1/2 week (d-d m y) Interpret and visualize the analysis results if needed
* 1/4 week (d-d m y) Draft the results report
* 1/2 week (d-d m y) Discuss the results with mentors
* 1/2 week (d-d m y) Report the results of the EP stage online (e.g. repo readme)

### HAP requirements
#### Skills required
* Knowledge of the embeddings theory and its mathematical backend


#### Sub-goals (~ 16 jan 2019 &ndash; 15 mar 2019)
* 3/2 week (d-d m y) Build embeddings for a pair of languages
* 2 wee (d-d m y)| Apply alignment technique described in [] (link) replacing the original idea of minimal-parallel-words-vocabulary with parallel phonemes vocabulary built on the idea of similarity of phonemes having 
    * the same glosses
    * similar hidden layer units activation levels
* 1 week (d-d m y) Evaluate the results
* 1 week (d-d m y) Analyze and interpret the results, visualize smth if needed
* 1/2 week (d-d m y) Draft the results report
* 1 week (d-d m y) Discuss the results with mentors
* 1 week (d-d m y) Report the results of the HAP stage in the paper format

## Data policy
The work should be continously published via GitHub repo under the MIT license.

## References
**TO-DO**
