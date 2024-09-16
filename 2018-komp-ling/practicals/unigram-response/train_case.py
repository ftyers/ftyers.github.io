import sys


def freq_list_for_tags(tags):
    count_tags: dict = {i: tags.count(i) for i in tags}
    number_of_tokens = sum(count_tags.values())
    p_column_tags = {}

    for i in count_tags:
        p = count_tags[i] / number_of_tokens
        p = round(p, 2)
        p_column_tags[i] = [p]

    for i in p_column_tags:
        if i in count_tags:
            p_column_tags[i].append(count_tags[i])

    titles = ['# P', 'count', 'tag', 'form']
    print('\t'.join(titles))
    for i in p_column_tags:
        print(str(p_column_tags[i][0]) + '\t' + str(p_column_tags[i][1]) + '\t' + i + '\t' + "-")
    return 0


def freq_list_for_words(words, tags_with_words):

    count_words = {i: words.count(i) for i in words}
    count_tags_with_words = {i: tags_with_words.count(i) for i in tags_with_words}

    for i in count_tags_with_words:
        freq_for_word_tag_pair = count_tags_with_words[i]
        tag_and_word = i.split('\t')
        tag = tag_and_word[0]
        word = tag_and_word[1]
        word_instances_total = count_words[word]
        p_for_word = freq_for_word_tag_pair / word_instances_total
        print(str(p_for_word) + '\t' + str(word_instances_total) + '\t' + tag + '\t' + word)
    return 0


def main():

    tags = []
    words = []
    tags_with_words = []

    for line in sys.stdin.readlines():
        if line.startswith('#'):
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        tags.append(row[3])
        words.append(row[1])
        tags_with_words.append(row[3] + '\t' + row[1].lower())  ##this way every word will get a lower case for the further analysis

    words = [i.lower() for i in words] #this way every word will get a lower case for the further analysis
    #and in the output we will get a sum of frequencies of the same words in lower and upper case


    freq_list_for_tags(tags)
    freq_list_for_words(words, tags_with_words)
    return 0

if __name__ == '__main__':
    main()