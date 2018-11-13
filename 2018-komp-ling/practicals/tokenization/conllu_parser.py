import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
from conllu import parse


with open('ja_gsd-ud-test.conllu') as f:
    test_text = f.read()

with open('correct_tokenized_test.txt', 'w') as f:
    for sentence in parse(test_text):
        f.write(' '.join([token['form'] for token in sentence]) + '\n')



'''def extract_dictionary(filename):
    result = list()
    for tokenlist in readfile(filename):
        for token in tokenlist:
            if len(token["form"]) > 1:
                result.append(token["form"])

    result = sorted(list(set(result)))
    return list(result)

print (extract_dictionary('ja_gsd-ud-test.conllu'))'''

'''with open('correct_tokenized_test.txt', 'w') as f:
    d = extract_dictionary('ja_gsd-ud-test.conllu')
    for i in d:
        f.write(d)'''