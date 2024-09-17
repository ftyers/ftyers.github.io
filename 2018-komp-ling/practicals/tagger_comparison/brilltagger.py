from nltk.tag import TrigramTagger, DefaultTagger, brill, brill_trainer, SequentialBackoffTagger, UnigramTagger, BigramTagger
from nltk.tokenize import word_tokenize


def corpus_prework(corpusfile):
    with open(corpusfile, "r", encoding="utf-8") as r:
        corpus = r.read()
        listcorpus = corpus.split("\n\n")
        listsentence = []
        for sentence in listcorpus:
            newsentence = sentence.split("\n")
            listsentence.append(newsentence)
        listtokens = []
        for index, tokens in enumerate(listsentence):
            for token in tokens:
                newtoken = token.split("\t")
                if len(newtoken) == 2:
                    listtokens.append(tuple(newtoken))
                elif len(newtoken) > 2:
                    listtokens.append((newtoken[0], newtoken[1]))
            listsentence.pop(index)
            listsentence.insert(index, listtokens)
            listtokens = []
        listsentence.pop()
        return listsentence


def tagger_default(corpus):
    default_tagger = DefaultTagger('NOUN')
    tagger1 = UnigramTagger(corpus, backoff=default_tagger)
    tagger2 = BigramTagger(corpus, backoff=tagger1)
    tagger3 = TrigramTagger(corpus, backoff=tagger2)
    return tagger3


def brill_tagger(initial_tagger, train_sents):
    templates = [brill.Template(brill.Pos([-1])),
                 brill.Template(brill.Pos([1])),
                 brill.Template(brill.Pos([-2])),
                 brill.Template(brill.Pos([2])),
                 brill.Template(brill.Pos([-2, -1])),
                 brill.Template(brill.Pos([1, 2])),
                 brill.Template(brill.Pos([-3, -2, -1])),
                 brill.Template(brill.Pos([1, 2, 3])),
                 brill.Template(brill.Pos([-1]), brill.Pos([1])),
                 brill.Template(brill.Word([-1])),
                 brill.Template(brill.Word([1])),
                 brill.Template(brill.Word([-2])),
                 brill.Template(brill.Word([2])),
                 brill.Template(brill.Word([-2, -1])),
                 brill.Template(brill.Word([1, 2])),
                 brill.Template(brill.Word([-3, -2, -1])),
                 brill.Template(brill.Word([1, 2, 3])),
                 brill.Template(brill.Word([-1]), brill.Word([1])), ]
    trainer = brill_trainer.BrillTaggerTrainer(initial_tagger, templates, deterministic=True)
    return trainer.train(train_sents)


def gotta_tag_em_all(tagger, file):
    with open(file, "r", encoding="utf-8") as r:
        final = []
        for sentence in r.readlines():
            tokens = word_tokenize(sentence)
            final.append(tagger.tag(tokens))
        return final


def file_writer(filename, content):
    with open(filename, "w+", encoding="utf-8") as r:
        for sentence in content:
            n = 0
            for token in sentence:
                n += 1
                r.write(str(n) + "\t" + str(token[0]) + "\t" + "_" + "\t" + str(token[1]) + "\t" "_" + "\t" + "_" + "\t" + str(n-1) + "\t" + "_" + "\t" + "_" + "\t" + "_" + "\n")
            r.write("\n")


if __name__ == "__main__":
    corpus = corpus_prework(r"./hunpos/fi_tdt-ud-train.conllu")
    t2 = tagger_default(corpus)
    t3 = brill_tagger(t2, corpus)
    file_writer("TriYesDef.txt", gotta_tag_em_all(t2, r"./hunpos/sentencetotag.txt"))
    file_writer("Brill.txt", gotta_tag_em_all(t3, r"./hunpos/sentencetotag.txt"))
