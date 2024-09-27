from collections import Counter
import sys

total_count = 0
tag_count = Counter()
word_tag = {}

# getting the name of the file from the terminal
filename = sys.argv[1]

with open(filename, "r", encoding="utf8") as f:
    for line in f:
        # we need only lines with words, so we skip others
        if line.startswith("#") or len(line) == 1:
            continue
        element = line.strip().split("\t")
        word = element[1]
        pos = element[3]
        # we check whether the word is in dictionary: if not we create an empty dict for that
        if word not in word_tag:
            word_tag[word] = Counter()
        # we fill the dict of the word with its POS and count the number of that word+POS
        word_tag[word][pos] += 1
        # we add POS tag and count it
        tag_count[pos] += 1
        # we count total amount of words we have
        total_count += 1

if __name__ == '__main__':
    # print the head of the table
    print('\t'.join(["# P", "count", "tag", "form"]))
    # print the dict of POS tags
    for tag, num in tag_count.items():
        print("{0:.2f}".format(num / total_count), end="\t")
        print(num, end="\t")
        print(tag, end="\t")
        print("_")
    # print the dict of word+POS
    for word, tag_num in word_tag.items():
        total_num = 0
        for each in tag_num.items():
            total_num += each[1]
        for tag, num in tag_num.items():
            print("{0:.2f}".format(num / total_num), end="\t")
            print(num, end="\t")
            print(tag, end="\t")
            print(word)
