import nltk
from collections import Counter

import conllu
# id, form, lemma, upostag, xpostag, feats (Case, Number...), head, deprel, deps, misc


def from_connlu_to_nltk(sentences):
    return [[(token['lemma'], token['upostag']) for token in sentence] for sentence in sentences]


def main():
    with open("UD_Finnish-TDT/fi_tdt-ud-train.conllu") as f:
        train_lines = f.read()

    with open("UD_Finnish-TDT/fi_tdt-ud-test.conllu") as f:
        test_lines = f.read()

    conllu_train_sentences = conllu.parse(train_lines)
    nltk_train_sentences = from_connlu_to_nltk(conllu_train_sentences)
    raw_train_sentences = [[word for word, tag in sentence] for sentence in nltk_train_sentences]

    conllu_test_sentences = conllu.parse(test_lines)
    nltk_test_sentences = from_connlu_to_nltk(conllu_test_sentences)
    raw_test_sentences = [[word for word, tag in sentence] for sentence in nltk_test_sentences]

    c = Counter(token['upostag'] for sentence in conllu_train_sentences for token in sentence)
    most_common_tag = c.most_common(1)[0][0]

    default_tagger = nltk.DefaultTagger(most_common_tag)
    unigram_tagger = nltk.UnigramTagger(nltk_train_sentences, backoff=default_tagger)
    bigram_tagger = nltk.BigramTagger(nltk_train_sentences, backoff=unigram_tagger)

    print("We have trained a bigram tagger that falls back to simpler taggers in case of emerbency.")
    print("It has performed with the accuracy of", bigram_tagger.evaluate(nltk_test_sentences))


if __name__ == "__main__":
    main()
