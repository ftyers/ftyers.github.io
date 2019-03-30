import fileinput
import nltk
from nltk.tokenize import sent_tokenize


def read_a_file(file_path):
    file = open(file_path, "r", encoding='UTF-8')

    data = file.read()

    return data

def segmentator(text):
    sent_tokenized_list = sent_tokenize(text)
    f = open('nltk_punkt_result.txt', 'w', encoding='utf-8')
    for i in sent_tokenized_list:
        f.write(i + '\n')
    print(sent_tokenized_list[:10])
    return f


def main():
    file = read_a_file('50random.txt')
    segment_text = segmentator(file)
    return segment_text


if __name__ == '__main__':
    main()