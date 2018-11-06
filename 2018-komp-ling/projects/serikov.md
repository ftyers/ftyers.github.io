# Compling project proposal

## Abstract
RE: extracting phonological rules from neural networks paper: Jennifer Rodd (1997) "Recurrent Neural-Network Learning of Phonological Regularities in Turkish". CoNLL97: Computational Natural Language Learning, http://www.aclweb.org/anthology/W97-1012

## Introduction
**TO-DO** the background of the problem to be solved or topic to be studied, with references for the low-background reader.

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

#### Sub-goals
* 1 week| Reproduce the dataset used in original paper
* 1/2 week| Reproduce the NNs used in original paper
* 1/2 week| Reproduce the training process used in original paper
* 1/2 week| Reproduce the NNs analysis described in original paper
* 1/4 week| Compare the reproduced and original results
* 1/4 week| Draft the results report
* 1/4 week| Discuss the results with mentors
* 1/4 week| Report the results of the MVP stage online (e.g. repo readme)

### EP requirements

#### Sub-goals
* 1 week| Collect the data to repeat the research on different languages data
* 1/4 week| Accomplish the ML part of the research
* 1/2 week| Accomplish the analysis part of the research
* 1/2 week| Interpret and visualize the analysis results if needed
* 1/4 week| Draft the results report
* 1/2 week| Discuss the results with mentors
* 1/2 week| Report the results of the EP stage online (e.g. repo readme)

### HAP requirements
#### Skills required
* Knowledge of the embeddings theory and its mathematical backend


#### Sub-goals
* 3/2 week| Build embeddings for a pair of languages
* 2 week| Apply alignment technique described in [] (link) replacing the original idea of minimal-parallel-words-vocabulary with parallel phonemes vocabulary built on the idea of similarity of phonemes having 
    * the same glosses
    * similar hidden layer units activation levels
* 1 week| Evaluate the results
* 1 week| Analyze and interpret the results, visualize smth if needed
* 1/2 week| Draft the results report
* 1 week| Discuss the results with mentors
* 1 week| Report the results of the HAP stage in the paper format

## Data policy
The work should be continously published via GitHub repo under the MIT license.

## References
**TO-DO**
