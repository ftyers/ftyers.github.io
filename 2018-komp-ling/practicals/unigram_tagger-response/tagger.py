import sys


def get_tags_from_model(model_file):

    # this function makes 2 dictionaries:
    # a tag-frequency one and word-tags&frequencies one

    tags_dict = {}
    words_dict = {}

    f = open(model_file, 'r')
    model = f.readlines()
    f.close()

    for line in model:
        if line.startswith("#"):
            continue
        row = line.strip().split('\t')
        if row[2] not in tags_dict:
            tags_dict[row[2]] = float(row[0])
        else:
            if row[3] not in words_dict:
                words_dict[row[3]] = [(row[2], float(row[0]))]
            else:
                words_dict[row[3]] += [(row[2], float(row[0]))]

    return tags_dict, words_dict


def get_max_tag(tags_dict):
    # choose the most frequent POS-tag in the model
    max_freq = max([i for i in tags_dict.values()])
    for tag, freq in tags_dict.items():
        if max_freq == freq:
            return tag


def get_max_word_tags(words_dict):
    # create a dictionary, where keys are words from the model
    # and values are most frequent tags for these words
    words_and_max_tags = {}
    for word in words_dict:
        if len(words_dict[word]) == 1:
            words_and_max_tags[word] = words_dict[word][0][0]
        elif len(words_dict[word]) > 1:
            tags = []
            for i in words_dict[word]:
                tags.append(i)
            max_tag = max([j[1] for j in tags])
            for tag in tags:
                if tag[1] == max_tag:
                    words_and_max_tags[word] = tag[0]
    return words_and_max_tags



def run_tagger(input_file, words, max_tag):

    f = open(input_file, "r")
    input_ = f.readlines()
    f.close()

    for line in input_:
        if line.startswith('#') or line == '\n':
            print(line.strip())
        else:
            row = line.strip().split('\t')
            if len(row) != 10:
                continue
            if row[1].lower() in words:
                row[3] = words[row[1].lower()]
            else:
                row[3] = max_tag
            print('\t'.join(row))

    f.close()


def main():
    model, input_file = sys.argv[1:]
    tags_dict, words_dict = get_tags_from_model(model)
    max_tag = get_max_tag(tags_dict)
    model_words = get_max_word_tags(words_dict)
    run_tagger(input_file, model_words, max_tag)


if __name__ == '__main__':
    main()
