from conllu import parse
import pandas as pd
import sys

text = parse('\n'.join(line for line in sys.stdin))

model = pd.read_csv(sys.argv[1], sep='\t')

def get_pos_tag_by_word(word):
    db = model[model.form == word]
    if len(db) == 0:
        return model.tag[model['count'][model['form'] == '_'].idxmax()]
    else:
        return db.tag[db['count'].idxmax()]

for sentence in text:
    for token in sentence:
        print(get_pos_tag_by_word(token['form']))
