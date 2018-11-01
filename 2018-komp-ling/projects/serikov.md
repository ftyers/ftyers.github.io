# Compling project proposal

RE: extracting phonological rules from neural networks paper: Jennifer Rodd (1997) "Recurrent Neural-Network Learning of Phonological Regularities in Turkish". CoNLL97: Computational Natural Language Learning, http://www.aclweb.org/anthology/W97-1012

## Abstract

## Introduction
the background of the problem to be solved or topic to be studied, with references for the low-background reader.

## Proposed goals

### MVP
* re-implement the paper
* release the code and documentation showing how to run it, and extract the graphs that she shows.

### EP
Run it with other languages in the Turkic family to see if their networks split the same way. She tries it for Turkish, but other Turkic languages have different vowel harmony systems, and Uzbek does not have vowel harmony at all.

### HAP
Apply the received knowledge of computational phonology and turkic languages in particular to solve the task of phonetic embeddings alignment without having good parallel corpus.

## Requirements
breaks each goal into sub-goals. Each sub-goal should be labeled with a brief list of anticipated skills required, with references for skills not already possessed by Applicants.

**NB!** Each sub-goal is accompanied with the documentation composing and sources publishing where needed.

**NB!** Goals may be changed on the run if necessary (e.g. smth unexpected discovered). All the possible changes should be discussed with mentors.

### MVP requirements
#### skills required
Brief knowledge of actual NN creating techniques.
Data preprocessing skills
Vizualization skill.

#### sub-goals
* Reproduce the dataset used in original paper
* Reproduce the NNs used in original paper
* Reproduce the training process used in original paper
* Reproduce the NNs analysis described in original paper
* Compare the reproduced and original results
* Draft the results report
* Discuss the results with mentors
* Report the results of the MVP stage online (e.g. repo readme)

### EP requirements

#### sub-goals
* Collect the data to repeat the research on different languages data
* Accomplish the ML part of the research
* Accomplish the analysis part of the research
* Interpret and visualize the analysis results if needed
* Draft the results report
* Discuss the results with mentors
* Report the results of the EP stage online (e.g. repo readme)

### HAP requirements
Knowledge of the embeddings theory and its mathematical backend


#### sub-goals
* Build embeddings for a pair of languages
* Apply alignment technique described in [] (link) replacing the original idea of minimal-parallel-words-vocabulary with parallel phonemes vocabulary built on the idea of similarity of phonemes having 
    * the same glosses
    * similar hidden layer units activation levels
* Evaluate the results
* Analyze and interpret the results, visualize smth if needed
* Draft the results report
* Discuss the results with mentors
* Report the results of the HAP stage in the paper format

## Data policy
The work is continously published via GitHub repo under the MIT license.

## References

