# Practical 3 - Morphological disambiguation
#### *Anastasia Nikiforova*

1. **Tagger Comparison**

For tagging, I used Polish corpus. The tagging algorithms I used: UDPipe, MarMoT

UDPipe results are in ```UDPipe_finnish_results.txt``` and ```UDPipe_polish.txt```, MarMoT results are in ```text.out.txt```.
MarMoT was qutie tricky to use and result tags are rather strange. For tagging I used a pre-trained model ```pl.marmot```

I hope it is the correct tagging.

2. **Constraint Grammar**

CG3 was quite difficult to understand at first, but http://visl.sdu.dk/~eckhard/powerpoint/CG3_Nodalida_dis.pdf made it a lot easier. 
After reading this tutorial, writing rules was intuitive.

Basically, I eliminated all incorrect tags of nouns (they follow each other, so I had to modify the rule Nominative-Accusative-Accusative into a constraint). Also, there is a constraint that doesn't allow a noun to be nominative when it follows a preposition.

I actually enjoyed this task! It is very formal and logical, which is great.

3. **Improving Perceptron Tagger**

The results of an improved perceptron is ```perceptron_results.txt```. There is also an excerpt from the original code, showing changes to ```_get_features.function```.

The best performance was when I changes the suffix-related parameters from [-3:] to [-2:]. Changing word-related parameters decreased the performance, even if combined with changed suffix-related parameters.
